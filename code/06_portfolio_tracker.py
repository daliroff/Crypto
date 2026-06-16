"""
06_portfolio_tracker.py
=======================
Mock crypto portfolio tracker: fetches live prices from Binance and shows
current value, P&L, and allocation for a pre-defined portfolio.

Key concepts
------------
  Cost basis     = amount * avg_buy_price
  Current value  = amount * current_price
  P&L ($)        = current_value - cost_basis
  P&L (%)        = P&L ($) / cost_basis * 100
  Allocation (%) = current_value / total_portfolio_value * 100

USDT is treated as a stablecoin pegged to $1.00 — no live price fetch needed.
"""

import os
import sys
import ccxt
import pandas as pd
import matplotlib.pyplot as plt


OUTPUT_FILE = 'portfolio.png'

PORTFOLIO = {
    'BTC':  {'amount': 0.5,   'avg_buy_price': 35_000.0},
    'ETH':  {'amount': 5.0,   'avg_buy_price':  2_000.0},
    'SOL':  {'amount': 50.0,  'avg_buy_price':     80.0},
    'BNB':  {'amount': 10.0,  'avg_buy_price':    250.0},
    'USDT': {'amount': 500.0, 'avg_buy_price':      1.0},
}


def fetch_prices(assets: list) -> dict:
    """
    Fetch current USD prices for each asset from Binance public API.
    USDT is returned as 1.0 (no network call needed).
    """
    exchange = ccxt.binance({'enableRateLimit': True})
    prices = {}

    for asset in assets:
        if asset == 'USDT':
            prices[asset] = 1.0
            continue
        symbol = f'{asset}/USDT'
        try:
            ticker = exchange.fetch_ticker(symbol)
            prices[asset] = ticker['last']
            print(f"  {symbol:<12} ${prices[asset]:>12,.4f}")
        except ccxt.BadSymbol:
            print(f"  [Warning] Could not fetch {symbol} — defaulting to 0")
            prices[asset] = 0.0

    return prices


def build_portfolio_df(portfolio: dict, prices: dict) -> pd.DataFrame:
    """Compute per-asset metrics and return a summary DataFrame."""
    rows = []
    for asset, data in portfolio.items():
        amount     = data['amount']
        buy_price  = data['avg_buy_price']
        curr_price = prices.get(asset, 0.0)
        cost_basis = amount * buy_price
        curr_value = amount * curr_price
        pnl_usd    = curr_value - cost_basis
        pnl_pct    = (pnl_usd / cost_basis * 100) if cost_basis > 0 else 0.0
        rows.append({
            'asset':         asset,
            'amount':        amount,
            'avg_buy_price': buy_price,
            'current_price': curr_price,
            'cost_basis':    cost_basis,
            'current_value': curr_value,
            'pnl_usd':       pnl_usd,
            'pnl_pct':       pnl_pct,
        })

    df = pd.DataFrame(rows)
    total_value = df['current_value'].sum()
    df['allocation_pct'] = df['current_value'] / total_value * 100
    return df


def print_portfolio_table(df: pd.DataFrame) -> None:
    """Print a formatted portfolio summary table."""
    total_value   = df['current_value'].sum()
    total_cost    = df['cost_basis'].sum()
    total_pnl     = total_value - total_cost
    total_pnl_pct = (total_pnl / total_cost * 100) if total_cost > 0 else 0.0

    header = (f"{'Asset':<6} {'Amount':>10} {'Avg Buy':>12} {'Current':>12} "
              f"{'Value':>12} {'P&L $':>11} {'P&L %':>8} {'Alloc%':>8}")
    sep = "=" * len(header)

    print(f"\n{sep}")
    print("PORTFOLIO SUMMARY")
    print(sep)
    print(header)
    print("-" * len(header))

    for _, row in df.iterrows():
        sign = '+' if row['pnl_usd'] >= 0 else ''
        print(
            f"{row['asset']:<6} "
            f"{row['amount']:>10.4f} "
            f"${row['avg_buy_price']:>11,.2f} "
            f"${row['current_price']:>11,.2f} "
            f"${row['current_value']:>11,.2f} "
            f"{sign}${row['pnl_usd']:>9,.2f} "
            f"{sign}{row['pnl_pct']:>6.1f}% "
            f"{row['allocation_pct']:>7.1f}%"
        )

    print("-" * len(header))
    sign = '+' if total_pnl >= 0 else ''
    print(
        f"{'TOTAL':<6} {'':>10} {'':>12} {'':>12} "
        f"${total_value:>11,.2f} "
        f"{sign}${total_pnl:>9,.2f} "
        f"{sign}{total_pnl_pct:>6.1f}% "
        f"{'100.0':>7}%"
    )
    print(sep)


def plot_portfolio_pie(df: pd.DataFrame, output_path: str) -> None:
    """Save a pie chart showing portfolio allocation by current value."""
    df_sorted = df.sort_values('current_value', ascending=False)

    labels = [
        f"{row['asset']}\n${row['current_value']:,.0f}\n({row['allocation_pct']:.1f}%)"
        for _, row in df_sorted.iterrows()
    ]
    sizes  = df_sorted['current_value'].values
    colors = ['#4C72B0', '#DD8452', '#55A868', '#C44E52', '#8172B2',
              '#937860', '#DA8BC3', '#8C8C8C'][:len(sizes)]

    fig, ax = plt.subplots(figsize=(9, 7))
    wedges, texts, autotexts = ax.pie(
        sizes, labels=labels, colors=colors,
        autopct='%1.1f%%', startangle=140,
        pctdistance=0.75, labeldistance=1.15,
        wedgeprops={'edgecolor': 'white', 'linewidth': 1.5}
    )
    for at in autotexts:
        at.set_fontsize(9)

    total_value = df['current_value'].sum()
    ax.set_title(f'Portfolio Allocation  (Total: ${total_value:,.2f})',
                 fontsize=14, fontweight='bold', pad=20)

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")


if __name__ == '__main__':
    script_dir  = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, OUTPUT_FILE)

    try:
        print("Fetching current prices from Binance...")
        assets = list(PORTFOLIO.keys())
        prices = fetch_prices(assets)

        df = build_portfolio_df(PORTFOLIO, prices)
        print_portfolio_table(df)
        plot_portfolio_pie(df, output_path)

    except ccxt.NetworkError as e:
        print(f"[Network Error] {e}")
        sys.exit(1)
    except Exception as e:
        print(f"[{type(e).__name__}] {e}")
        sys.exit(1)
