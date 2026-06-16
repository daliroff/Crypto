"""
07_dca_simulator.py
===================
Simulate and compare Dollar-Cost Averaging (DCA) vs Lump-Sum investing in BTC.

What is Dollar-Cost Averaging (DCA)?
-------------------------------------
DCA is an investment strategy where you invest a fixed dollar amount at regular
intervals (e.g., $200 every week), regardless of the asset's price.

How DCA works mathematically:
  Week 1: Price = $40,000 → $200 / $40,000 = 0.005000 BTC
  Week 2: Price = $38,000 → $200 / $38,000 = 0.005263 BTC  (more BTC, lower price)
  Week 3: Price = $42,000 → $200 / $42,000 = 0.004762 BTC  (less BTC, higher price)
  → You automatically buy MORE when cheap and LESS when expensive.

Average Buy Price:
  avg_price = total_USD_spent / total_BTC_accumulated
  This is the "average cost basis" — lower is better.

What is Lump-Sum Investing?
---------------------------
Lump-sum means investing ALL your capital at once, at the very beginning.
  Total $10,400 → invest on Day 1 → fixed BTC amount forever.

DCA vs Lump-Sum — When does each win?
--------------------------------------
  DCA wins when:
    - The asset FALLS after you start investing (you average down)
    - The market is volatile / uncertain
    - You don't have all capital available at once (regular income)
    - It reduces the psychological burden of "timing the market"

  Lump-Sum wins when:
    - The asset RISES consistently after Day 1 (missed gains from staged entry)
    - Historically, ~70% of the time markets trend upward long-term

  The key insight: DCA is about RISK MANAGEMENT and discipline, not
  maximizing returns. It protects against buying everything at the top.

Simulation Parameters:
----------------------
  Total capital : $10,400
  Weekly invest : $200
  Duration      : 52 weeks (1 year)
  Asset         : BTC/USDT
"""

import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


TOTAL_INVESTMENT = 10_400.0   # Total USD to invest
WEEKLY_AMOUNT    = 200.0      # USD invested each week (DCA)
NUM_WEEKS        = 52         # Duration in weeks


def load_or_generate_prices(script_dir: str) -> pd.DataFrame:
    """
    Load BTC daily price data from btc_usdt_daily.csv if it exists,
    otherwise generate a synthetic random walk.

    Parameters
    ----------
    script_dir : Directory to look for the CSV file

    Returns
    -------
    pd.DataFrame with DatetimeIndex and 'close' column (at least 365 rows)
    """
    csv_path = os.path.join(script_dir, 'btc_usdt_daily.csv')

    if os.path.exists(csv_path):
        print(f"Loading price data from {csv_path}")
        df = pd.read_csv(csv_path, parse_dates=['timestamp'])
        df = df.set_index('timestamp').sort_index()
        print(f"Loaded {len(df)} rows ({df.index[0].date()} → {df.index[-1].date()})")

        # Make sure we have at least 365 rows (one year)
        if len(df) >= 365:
            # Use the most recent 365 days
            df = df.tail(365)
            return df[['close']].copy()
        else:
            print(f"Only {len(df)} rows available — supplementing with synthetic data.")
            # Fall through to synthetic generation below

    # --- Synthetic Price Generation ---
    # Generate a realistic random walk with drift to simulate BTC price
    print("Generating synthetic BTC price data (random walk with drift)...")

    np.random.seed(42)          # Reproducible results
    n_days      = 365
    start_price = 40_000.0     # Starting BTC price in USDT
    daily_vol   = 0.03         # 3% daily volatility (realistic for BTC)
    daily_drift = 0.0003       # ~11% annualized upward drift

    # Geometric Brownian Motion: the standard model for stock/crypto prices
    # Price_{t+1} = Price_t * exp(drift + volatility * Z)
    # where Z is a standard normal random variable
    returns = np.random.normal(loc=daily_drift, scale=daily_vol, size=n_days)
    prices  = start_price * np.exp(np.cumsum(returns))

    # Add a small mean-reversion component to keep prices realistic
    prices = np.clip(prices, start_price * 0.3, start_price * 5)

    dates = pd.date_range(start='2023-01-01', periods=n_days, freq='D')
    df    = pd.DataFrame({'close': prices}, index=dates)

    print(f"Generated {n_days} synthetic daily prices: ${prices[0]:,.0f} → ${prices[-1]:,.0f}")
    return df


def sample_weekly_prices(df: pd.DataFrame) -> pd.DataFrame:
    """
    Resample daily prices to weekly by taking every 7th row.

    Parameters
    ----------
    df : Daily OHLCV-style DataFrame with 'close' column

    Returns
    -------
    pd.DataFrame with weekly prices (52 rows for one year)
    """
    # Take every 7th row starting from the first (indices 0, 7, 14, ...)
    weekly = df.iloc[::7].copy().head(NUM_WEEKS)
    weekly.index.name = 'date'
    return weekly


def simulate_dca(weekly_prices: pd.DataFrame, weekly_amount: float) -> pd.DataFrame:
    """
    Simulate the DCA strategy week by week.

    For each week:
      - Spend a fixed $weekly_amount at that week's BTC price
      - Accumulate BTC bought and USD spent

    Parameters
    ----------
    weekly_prices : DataFrame with 'close' column (weekly BTC prices)
    weekly_amount : USD to invest each week

    Returns
    -------
    DataFrame with DCA simulation columns
    """
    results = []
    total_btc  = 0.0
    total_usd  = 0.0

    for i, (date, row) in enumerate(weekly_prices.iterrows()):
        price = row['close']

        # Amount of BTC purchased this week = USD invested / price
        btc_bought = weekly_amount / price
        total_btc  += btc_bought
        total_usd  += weekly_amount

        # Average cost basis = total USD spent / total BTC accumulated
        avg_cost = total_usd / total_btc if total_btc > 0 else 0.0

        # Current portfolio value = total BTC * current price
        portfolio_value = total_btc * price

        results.append({
            'date':           date,
            'price':          price,
            'week':           i + 1,
            'btc_bought':     btc_bought,
            'total_btc_dca':  total_btc,
            'total_usd_dca':  total_usd,
            'avg_cost_dca':   avg_cost,
            'value_dca':      portfolio_value,
        })

    return pd.DataFrame(results).set_index('date')


def simulate_lumpsum(weekly_prices: pd.DataFrame, total_investment: float) -> pd.DataFrame:
    """
    Simulate lump-sum investing: buy all at Week 1, hold through Week 52.

    Parameters
    ----------
    weekly_prices    : DataFrame with weekly 'close' prices
    total_investment : Total USD to invest on Day 1

    Returns
    -------
    DataFrame with lump-sum value column
    """
    # Buy all BTC at the first week's price
    first_price = weekly_prices['close'].iloc[0]
    total_btc   = total_investment / first_price

    print(f"\nLump-Sum: Bought {total_btc:.6f} BTC at ${first_price:,.2f} on Week 1")

    # Track portfolio value week by week (fixed BTC amount, changing price)
    values = weekly_prices['close'] * total_btc
    return values.rename('value_lumpsum')


def plot_comparison(
    dca_df: pd.DataFrame,
    ls_series: pd.Series,
    weekly_prices: pd.DataFrame,
    output_path: str
) -> None:
    """
    Create a 2x2 comparison chart.

    Layout:
      [Top-Left]     BTC price over the year
      [Top-Right]    Portfolio value: DCA vs Lump-Sum
      [Bottom-Left]  Cumulative BTC accumulated (DCA vs Lump-Sum)
      [Bottom-Right] Average cost basis vs current price (DCA)
    """
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    (ax1, ax2), (ax3, ax4) = axes

    # ---- Top-Left: BTC Price ----
    ax1.plot(weekly_prices.index, weekly_prices['close'],
             color='steelblue', linewidth=2, marker='o', markersize=3)
    ax1.set_title('BTC Price Over 52 Weeks', fontsize=12, fontweight='bold')
    ax1.set_ylabel('BTC Price (USDT)', fontsize=10)
    ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${x:,.0f}'))
    ax1.grid(True, alpha=0.3, linestyle='--')
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
    ax1.xaxis.set_major_locator(mdates.MonthLocator(interval=2))

    # ---- Top-Right: Portfolio Value ----
    ax2.plot(dca_df.index, dca_df['value_dca'],
             color='limegreen', linewidth=2.5, label='DCA ($200/week)')
    ax2.plot(ls_series.index, ls_series,
             color='darkorange', linewidth=2.5, linestyle='--', label='Lump Sum ($10,400)')

    # Horizontal line at total invested ($10,400)
    ax2.axhline(y=TOTAL_INVESTMENT, color='gray', linestyle=':', linewidth=1.0,
                label=f'Invested = ${TOTAL_INVESTMENT:,.0f}')

    ax2.set_title('Portfolio Value: DCA vs Lump Sum', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Portfolio Value (USDT)', fontsize=10)
    ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${x:,.0f}'))
    ax2.legend(fontsize=9)
    ax2.grid(True, alpha=0.3, linestyle='--')
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
    ax2.xaxis.set_major_locator(mdates.MonthLocator(interval=2))

    # ---- Bottom-Left: Cumulative BTC Accumulated ----
    # DCA: gradually accumulates BTC every week
    lumpsum_first_price = weekly_prices['close'].iloc[0]
    lumpsum_btc = TOTAL_INVESTMENT / lumpsum_first_price

    ax3.plot(dca_df.index, dca_df['total_btc_dca'],
             color='limegreen', linewidth=2.5, label='DCA (accumulated weekly)')
    ax3.axhline(y=lumpsum_btc, color='darkorange', linestyle='--', linewidth=2.0,
                label=f'Lump Sum (fixed: {lumpsum_btc:.5f} BTC)')
    ax3.set_title('Cumulative BTC Accumulated', fontsize=12, fontweight='bold')
    ax3.set_ylabel('BTC Amount', fontsize=10)
    ax3.legend(fontsize=9)
    ax3.grid(True, alpha=0.3, linestyle='--')
    ax3.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
    ax3.xaxis.set_major_locator(mdates.MonthLocator(interval=2))

    # ---- Bottom-Right: Average Cost Basis vs Current Price (DCA) ----
    ax4.plot(dca_df.index, dca_df['price'],
             color='steelblue', linewidth=1.5, label='BTC Market Price', alpha=0.7)
    ax4.plot(dca_df.index, dca_df['avg_cost_dca'],
             color='crimson', linewidth=2.5, linestyle='--', label='DCA Avg Cost Basis')
    ax4.fill_between(dca_df.index,
                     dca_df['avg_cost_dca'], dca_df['price'],
                     where=(dca_df['price'] >= dca_df['avg_cost_dca']),
                     alpha=0.15, color='green', label='In Profit Zone')
    ax4.fill_between(dca_df.index,
                     dca_df['avg_cost_dca'], dca_df['price'],
                     where=(dca_df['price'] < dca_df['avg_cost_dca']),
                     alpha=0.15, color='red', label='In Loss Zone')
    ax4.set_title('DCA: Average Cost Basis vs Market Price', fontsize=12, fontweight='bold')
    ax4.set_ylabel('Price (USDT)', fontsize=10)
    ax4.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${x:,.0f}'))
    ax4.legend(fontsize=9)
    ax4.grid(True, alpha=0.3, linestyle='--')
    ax4.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
    ax4.xaxis.set_major_locator(mdates.MonthLocator(interval=2))

    # Rotate x-axis labels on all subplots
    for ax in axes.flat:
        plt.setp(ax.xaxis.get_majorticklabels(), rotation=30, ha='right', fontsize=8)

    plt.suptitle('DCA vs Lump Sum — BTC Investment Simulation (52 Weeks)',
                 fontsize=15, fontweight='bold', y=1.01)
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")


def print_comparison_table(dca_df: pd.DataFrame, ls_series: pd.Series) -> None:
    """Print a side-by-side comparison of DCA vs Lump-Sum outcomes."""
    # DCA final stats
    dca_final_value  = dca_df['value_dca'].iloc[-1]
    dca_total_spent  = dca_df['total_usd_dca'].iloc[-1]
    dca_return_pct   = (dca_final_value / dca_total_spent - 1) * 100
    dca_avg_cost     = dca_df['avg_cost_dca'].iloc[-1]
    dca_final_btc    = dca_df['total_btc_dca'].iloc[-1]

    # Lump-Sum final stats
    ls_final_value   = ls_series.iloc[-1]
    ls_return_pct    = (ls_final_value / TOTAL_INVESTMENT - 1) * 100

    final_price      = dca_df['price'].iloc[-1]
    first_price      = dca_df['price'].iloc[0]

    print("\n" + "=" * 65)
    print("  DCA vs LUMP SUM — FINAL COMPARISON")
    print("=" * 65)
    print(f"  {'Metric':<30} {'DCA':>15} {'Lump Sum':>15}")
    print("  " + "-" * 61)
    print(f"  {'Total Invested':<30} {'$'+f'{dca_total_spent:,.0f}':>15} {'$'+f'{TOTAL_INVESTMENT:,.0f}':>15}")
    print(f"  {'Final Portfolio Value':<30} {'$'+f'{dca_final_value:,.0f}':>15} {'$'+f'{ls_final_value:,.0f}':>15}")
    print(f"  {'Return (%)':<30} {dca_return_pct:>+14.2f}% {ls_return_pct:>+14.2f}%")
    print(f"  {'Profit / Loss ($)':<30} {'$'+f'{dca_final_value - dca_total_spent:+,.0f}':>15} {'$'+f'{ls_final_value - TOTAL_INVESTMENT:+,.0f}':>15}")
    print(f"  {'BTC Accumulated':<30} {dca_final_btc:>15.6f} {TOTAL_INVESTMENT/first_price:>15.6f}")
    print(f"  {'Avg Buy Price':<30} {'$'+f'{dca_avg_cost:,.2f}':>15} {'$'+f'{first_price:,.2f}':>15}")
    print(f"  {'Final BTC Price':<30} {'$'+f'{final_price:,.2f}':>15} {'$'+f'{final_price:,.2f}':>15}")
    print("=" * 65)

    winner = "DCA" if dca_final_value > ls_final_value else "Lump Sum"
    diff   = abs(dca_final_value - ls_final_value)
    print(f"\n  WINNER this period: {winner} by ${diff:,.0f}")
    print()
    if winner == "Lump Sum":
        print("  In a rising market, lump-sum typically wins because you")
        print("  own more BTC from Day 1 and benefit from more upside.")
    else:
        print("  DCA won here because the price dipped early, allowing")
        print("  you to accumulate more BTC at lower average cost.")
    print("=" * 65)


if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.abspath(__file__))
    chart_path = os.path.join(script_dir, 'dca_simulator.png')

    try:
        # Load or generate 365 days of daily prices
        daily_df = load_or_generate_prices(script_dir)

        # Resample to weekly (every 7th row)
        weekly_prices = sample_weekly_prices(daily_df)
        print(f"Weekly prices sampled: {len(weekly_prices)} weeks")

        # Run DCA simulation
        dca_df = simulate_dca(weekly_prices, weekly_amount=WEEKLY_AMOUNT)

        # Run Lump-Sum simulation
        ls_series = simulate_lumpsum(weekly_prices, total_investment=TOTAL_INVESTMENT)

        # Print comparison
        print_comparison_table(dca_df, ls_series)

        # Generate charts
        plot_comparison(dca_df, ls_series, weekly_prices, output_path=chart_path)

    except Exception as e:
        print(f"[Unexpected Error] {type(e).__name__}: {e}")
        sys.exit(1)
