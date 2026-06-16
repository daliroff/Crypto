"""
05_backtest_sma_crossover.py
============================
SMA(20)/SMA(50) crossover backtest on 3 years of BTC/USDT daily data.

Strategy rules
--------------
  BUY  when SMA(20) crosses above SMA(50)  ← golden cross
  SELL when SMA(20) crosses below SMA(50)  ← death cross

  We hold a full position (no fractional shares). When a buy signal fires
  we invest the entire portfolio at that day's close price. When a sell
  signal fires we liquidate the full position at close.

Look-ahead bias prevention
---------------------------
  Signals are generated on day T but executed at day T+1 close.
  In the vectorised path this is handled by shifting the position series.
  In the explicit trade-log path we record execution one row after the
  crossover row.

Metrics reported
----------------
  Total return %        — strategy vs buy-and-hold
  Sharpe ratio          — annualised, risk-free rate = 0
  Max drawdown %        — largest peak-to-trough decline
  Win rate %            — % of closed trades that were profitable
"""

import os
import sys
import numpy as np
import ccxt
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


CSV_FILE    = 'btc_ohlcv.csv'
OUTPUT_FILE = 'backtest_results.png'
INITIAL_CASH = 10_000.0
FAST, SLOW   = 20, 50


def load_or_fetch(script_dir: str, limit: int = 1095) -> pd.DataFrame:
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
    # Use the most recent `limit` rows in case the CSV has more
    df = df.iloc[-limit:]
    print(f"Using {len(df)} rows  ({df.index[0].date()} → {df.index[-1].date()})")
    return df


def run_backtest(df: pd.DataFrame) -> tuple[pd.DataFrame, list[dict]]:
    """
    Execute the SMA crossover strategy and return:
      - df enriched with equity-curve columns
      - trade_log list of dicts

    Position is entered/exited at the NEXT day's close after the crossover
    (shift(1) prevents look-ahead bias).
    """
    df = df.copy()
    df['sma20'] = df['close'].rolling(FAST).mean()
    df['sma50'] = df['close'].rolling(SLOW).mean()

    # Raw signal: 1 = long, 0 = flat
    df['raw_signal'] = np.where(df['sma20'] > df['sma50'], 1, 0)
    # Shift by 1: we trade at next day's close once the signal is confirmed
    df['position'] = df['raw_signal'].shift(1).fillna(0)

    # ---- Explicit trade log (full position, no fractions) ----
    trade_log = []
    cash      = INITIAL_CASH
    btc_held  = 0.0
    in_trade  = False
    entry_price = 0.0

    for date, row in df.iterrows():
        price = row['close']
        pos   = row['position']

        if pos == 1 and not in_trade:
            # BUY — deploy all cash
            btc_held    = cash / price
            entry_price = price
            cash        = 0.0
            in_trade    = True
            portfolio_val = btc_held * price
            trade_log.append({'date': date, 'action': 'BUY',
                               'price': price, 'portfolio_value': portfolio_val})

        elif pos == 0 and in_trade:
            # SELL — liquidate full position
            cash      = btc_held * price
            btc_held  = 0.0
            in_trade  = False
            trade_log.append({'date': date, 'action': 'SELL',
                               'price': price, 'portfolio_value': cash})

    # Mark-to-market portfolio value for equity curve
    portfolio_values = []
    cash_sim  = INITIAL_CASH
    btc_sim   = 0.0
    in_trade_sim = False
    for date, row in df.iterrows():
        pos   = row['position']
        price = row['close']
        if pos == 1 and not in_trade_sim:
            btc_sim      = cash_sim / price
            cash_sim     = 0.0
            in_trade_sim = True
        elif pos == 0 and in_trade_sim:
            cash_sim     = btc_sim * price
            btc_sim      = 0.0
            in_trade_sim = False
        portfolio_values.append(cash_sim + btc_sim * price)

    df['equity'] = portfolio_values
    df['bh_equity'] = INITIAL_CASH * df['close'] / df['close'].iloc[0]

    return df, trade_log


def compute_metrics(df: pd.DataFrame, trade_log: list[dict]) -> dict:
    """Compute summary statistics from the equity curve and trade log."""
    equity = df['equity'].dropna()
    bh     = df['bh_equity'].dropna()

    total_return = (equity.iloc[-1] / INITIAL_CASH - 1) * 100
    bh_return    = (bh.iloc[-1]     / INITIAL_CASH - 1) * 100

    daily_ret = equity.pct_change().dropna()
    sharpe    = (daily_ret.mean() / daily_ret.std() * np.sqrt(252)
                 if daily_ret.std() > 0 else 0.0)

    running_max  = equity.cummax()
    drawdowns    = (equity - running_max) / running_max
    max_drawdown = drawdowns.min() * 100

    # Win rate: compare consecutive BUY/SELL pairs
    sells = [t for t in trade_log if t['action'] == 'SELL']
    buys  = [t for t in trade_log if t['action'] == 'BUY']
    wins  = sum(1 for b, s in zip(buys, sells) if s['price'] > b['price'])
    num_trades = len(sells)
    win_rate   = (wins / num_trades * 100) if num_trades else 0.0

    return {
        'total_return': total_return,
        'bh_return':    bh_return,
        'sharpe':       sharpe,
        'max_drawdown': max_drawdown,
        'win_rate':     win_rate,
        'num_trades':   num_trades,
        'final_value':  equity.iloc[-1],
    }


def print_results(metrics: dict, trade_log: list[dict]) -> None:
    """Print trade log and summary statistics table."""
    print("\nTRADE LOG")
    print(f"{'Date':<12} {'Action':<6} {'Price':>12} {'Portfolio':>14}")
    print("-" * 48)
    for t in trade_log:
        print(f"{str(t['date'].date()):<12} {t['action']:<6} "
              f"${t['price']:>11,.2f} ${t['portfolio_value']:>13,.2f}")

    print("\n" + "=" * 48)
    print(f"  {'Metric':<28} {'Value':>12}")
    print("=" * 48)
    print(f"  {'Strategy Total Return':<28} {metrics['total_return']:>11.2f}%")
    print(f"  {'Buy-and-Hold Return':<28} {metrics['bh_return']:>11.2f}%")
    print(f"  {'Sharpe Ratio (annualised)':<28} {metrics['sharpe']:>12.2f}")
    print(f"  {'Max Drawdown':<28} {metrics['max_drawdown']:>11.2f}%")
    print(f"  {'Win Rate':<28} {metrics['win_rate']:>11.1f}%")
    print(f"  {'Number of Trades':<28} {metrics['num_trades']:>12}")
    print(f"  {'Final Portfolio Value':<28} ${metrics['final_value']:>11,.2f}")
    print("=" * 48)


def plot_backtest(df: pd.DataFrame, output_path: str) -> None:
    """Plot equity curve (strategy vs buy-and-hold)."""
    fig, ax = plt.subplots(figsize=(14, 6))

    ax.plot(df.index, df['equity'],    color='limegreen',  linewidth=2.0,
            label='SMA(20/50) Crossover Strategy')
    ax.plot(df.index, df['bh_equity'], color='steelblue',  linewidth=2.0,
            linestyle='--', label='Buy and Hold')
    ax.axhline(INITIAL_CASH, color='gray', linewidth=0.8, linestyle=':', alpha=0.6)

    ax.set_title('BTC/USDT — SMA(20/50) Crossover Backtest: Equity Curve',
                 fontsize=14, fontweight='bold', pad=12)
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Portfolio Value (USD)', fontsize=12)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${x:,.0f}'))
    ax.legend(fontsize=11)
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
        df = load_or_fetch(script_dir, limit=1095)
        df, trade_log = run_backtest(df)
        metrics = compute_metrics(df, trade_log)
        print_results(metrics, trade_log)
        plot_backtest(df, output_path)

    except ccxt.NetworkError as e:
        print(f"[Network Error] {e}")
        sys.exit(1)
    except Exception as e:
        print(f"[{type(e).__name__}] {e}")
        sys.exit(1)
