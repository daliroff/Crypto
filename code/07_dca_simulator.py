"""
07_dca_simulator.py
===================
DCA vs lump-sum simulator using 2 years of real BTC/USDT daily price data.

Dollar-Cost Averaging (DCA)
----------------------------
Invest a fixed amount ($100) every week on Monday, buying at that day's close.
You automatically buy more BTC when prices are low and less when high.

Lump-Sum
---------
Invest the full equivalent capital (num_weeks * $100) on day 1.

When each strategy wins
------------------------
  DCA wins       — when the price falls after you start (you accumulate cheaper)
  Lump-sum wins  — when the price rises consistently from day 1
                   (you own the full position from the start)

DCA is primarily a risk-management tool, not a return maximiser.
"""

import os
import sys
import ccxt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


CSV_FILE      = 'btc_ohlcv.csv'
OUTPUT_FILE   = 'dca_vs_lumpsum.png'
WEEKLY_AMOUNT = 100.0   # USD invested each week under DCA


def load_or_fetch(script_dir: str, limit: int = 730) -> pd.DataFrame:
    """Return OHLCV DataFrame for the requested number of days."""
    csv_path = os.path.join(script_dir, CSV_FILE)

    if os.path.exists(csv_path):
        print(f"Loading data from {csv_path}")
        df = pd.read_csv(csv_path, parse_dates=['timestamp'])
    else:
        print("CSV not found — fetching from Binance...")
        exchange = ccxt.binance({'enableRateLimit': True})
        raw = exchange.fetch_ohlcv('BTC/USDT', timeframe='1d', since=None, limit=limit)
        df = pd.DataFrame(raw, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        df.to_csv(csv_path, index=False)
        print(f"Saved {len(df)} rows to {csv_path}")

    df = df.sort_values('timestamp').reset_index(drop=True)
    df = df.set_index('timestamp')
    # Use the most recent `limit` rows
    df = df.iloc[-limit:]
    print(f"Using {len(df)} rows  ({df.index[0].date()} → {df.index[-1].date()})")
    return df


def get_mondays(df: pd.DataFrame) -> pd.DataFrame:
    """Return rows where the index falls on a Monday (weekday == 0)."""
    return df[df.index.weekday == 0].copy()


def simulate_dca(df: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    """
    Simulate DCA: invest $100 every Monday at that day's close.

    Returns
    -------
    portfolio_df : daily mark-to-market portfolio value
    stats        : summary dict
    """
    mondays = get_mondays(df)
    num_weeks = len(mondays)

    total_btc = 0.0
    total_usd = 0.0
    buy_dates = []

    for date, row in mondays.iterrows():
        price      = row['close']
        btc_bought = WEEKLY_AMOUNT / price
        total_btc += btc_bought
        total_usd += WEEKLY_AMOUNT
        buy_dates.append(date)

    # Daily mark-to-market: how much is our DCA stack worth each day?
    # We re-compute by replaying purchases day by day
    btc_running = 0.0
    usd_running = 0.0
    monday_set  = set(mondays.index)
    daily_values = []

    for date, row in df.iterrows():
        if date in monday_set:
            btc_running += WEEKLY_AMOUNT / row['close']
            usd_running += WEEKLY_AMOUNT
        daily_values.append(btc_running * row['close'])

    portfolio = df[['close']].copy()
    portfolio['dca_value'] = daily_values

    stats = {
        'total_invested': total_usd,
        'final_value':    daily_values[-1],
        'roi_pct':        (daily_values[-1] / total_usd - 1) * 100,
        'num_trades':     num_weeks,
    }
    return portfolio, stats


def simulate_lumpsum(df: pd.DataFrame, total_invested: float) -> tuple[pd.Series, dict]:
    """
    Simulate lump-sum: invest the full amount on day 1 at close price.

    Returns
    -------
    ls_values : daily portfolio value series
    stats     : summary dict
    """
    first_price = df['close'].iloc[0]
    btc_held    = total_invested / first_price
    ls_values   = df['close'] * btc_held

    stats = {
        'total_invested': total_invested,
        'final_value':    ls_values.iloc[-1],
        'roi_pct':        (ls_values.iloc[-1] / total_invested - 1) * 100,
        'num_trades':     1,
    }
    return ls_values, stats


def print_stats(dca_stats: dict, ls_stats: dict) -> None:
    """Print final comparison table."""
    print("\n" + "=" * 56)
    print(f"  {'Metric':<28} {'DCA':>12} {'Lump-Sum':>12}")
    print("=" * 56)
    print(f"  {'Total Invested':<28} ${dca_stats['total_invested']:>11,.2f} ${ls_stats['total_invested']:>11,.2f}")
    print(f"  {'Final Value':<28} ${dca_stats['final_value']:>11,.2f} ${ls_stats['final_value']:>11,.2f}")
    print(f"  {'ROI %':<28} {dca_stats['roi_pct']:>11.2f}% {ls_stats['roi_pct']:>11.2f}%")
    print(f"  {'Number of Trades':<28} {dca_stats['num_trades']:>12} {ls_stats['num_trades']:>12}")
    print("=" * 56)
    winner = 'DCA' if dca_stats['final_value'] > ls_stats['final_value'] else 'Lump-Sum'
    diff   = abs(dca_stats['final_value'] - ls_stats['final_value'])
    print(f"\n  Winner: {winner}  (by ${diff:,.2f})")


def plot_dca_vs_lumpsum(portfolio: pd.DataFrame, ls_values: pd.Series,
                        dca_stats: dict, ls_stats: dict, output_path: str) -> None:
    """Plot both equity curves on the same chart."""
    fig, ax = plt.subplots(figsize=(14, 6))

    ax.plot(portfolio.index, portfolio['dca_value'], color='limegreen', linewidth=2.0,
            label=f"DCA ($100/week)  — Final: ${dca_stats['final_value']:,.0f}")
    ax.plot(ls_values.index,  ls_values,             color='steelblue',  linewidth=2.0,
            linestyle='--',
            label=f"Lump-Sum        — Final: ${ls_stats['final_value']:,.0f}")

    # Mark DCA invested amount as a dotted reference line
    ax.axhline(dca_stats['total_invested'], color='gray', linewidth=0.9,
               linestyle=':', alpha=0.7, label=f"Total Invested: ${dca_stats['total_invested']:,.0f}")

    ax.set_title('BTC/USDT — DCA vs Lump-Sum (2 Years)',
                 fontsize=14, fontweight='bold', pad=12)
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Portfolio Value (USD)', fontsize=12)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${x:,.0f}'))
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3, linestyle='--')

    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
    fig.autofmt_xdate(rotation=30)

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")


if __name__ == '__main__':
    script_dir  = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, OUTPUT_FILE)

    try:
        df = load_or_fetch(script_dir, limit=730)

        portfolio, dca_stats = simulate_dca(df)
        total_invested = dca_stats['total_invested']   # num_weeks * $100

        ls_values, ls_stats = simulate_lumpsum(df, total_invested)

        print_stats(dca_stats, ls_stats)
        plot_dca_vs_lumpsum(portfolio, ls_values, dca_stats, ls_stats, output_path)

    except ccxt.NetworkError as e:
        print(f"[Network Error] {e}")
        sys.exit(1)
    except Exception as e:
        print(f"[{type(e).__name__}] {e}")
        sys.exit(1)
