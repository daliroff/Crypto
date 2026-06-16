"""
06_portfolio_tracker.py
=======================
A mock crypto portfolio tracker that fetches live prices and computes P&L.

What this script does:
----------------------
  1. Defines a mock portfolio with 6 crypto assets
  2. Fetches current market prices from Binance via ccxt
  3. Falls back to hardcoded prices if the network is unavailable
  4. Computes unrealized P&L for each holding
  5. Visualizes the portfolio as a pie chart + P&L bar chart
  6. Prints a formatted portfolio table

Key Concepts:
-------------
  Cost Basis   : Total amount you paid for an asset
                 cost_basis = amount * avg_buy_price

  Current Value: What your holding is worth right now
                 current_value = amount * current_price

  P&L ($)      : Unrealized profit/loss in dollar terms
                 pnl_usd = current_value - cost_basis

  P&L (%)      : Percentage gain or loss relative to cost
                 pnl_pct = (pnl_usd / cost_basis) * 100

  Portfolio Allocation: Each asset's share of total portfolio value
                 allocation = (current_value / total_value) * 100

Unrealized vs Realized P&L:
----------------------------
  Unrealized P&L: The gain/loss on holdings you still own (on paper)
  Realized P&L:   The actual gain/loss from positions you have closed
  This tracker shows UNREALIZED P&L only.
"""

import os
import sys
import ccxt
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker


# ---------------------------------------------------------------------------
# Mock Portfolio Definition
# ---------------------------------------------------------------------------
# Keys are base assets. avg_buy_price is in USDT. amount is in the base asset.
PORTFOLIO: dict = {
    'BTC':  {'amount': 0.5,    'avg_buy_price': 45000.0},
    'ETH':  {'amount': 5.0,    'avg_buy_price': 2800.0},
    'SOL':  {'amount': 50.0,   'avg_buy_price': 120.0},
    'BNB':  {'amount': 10.0,   'avg_buy_price': 300.0},
    'ADA':  {'amount': 2000.0, 'avg_buy_price': 0.45},
    'LINK': {'amount': 100.0,  'avg_buy_price': 15.0},
}

# Fallback prices (used if Binance is unreachable)
# These are approximate mid-2024 prices — update as needed
FALLBACK_PRICES: dict = {
    'BTC':  62000.0,
    'ETH':  3400.0,
    'SOL':  155.0,
    'BNB':  580.0,
    'ADA':  0.48,
    'LINK': 17.5,
}


def fetch_live_prices(assets: list) -> dict:
    """
    Fetch current USDT prices for each asset from Binance.

    Parameters
    ----------
    assets : list of asset symbols, e.g. ['BTC', 'ETH', 'SOL']

    Returns
    -------
    dict mapping symbol → current price in USDT
    """
    exchange = ccxt.binance({'enableRateLimit': True})
    prices = {}

    print("Fetching live prices from Binance...")
    for asset in assets:
        symbol = f'{asset}/USDT'
        try:
            ticker = exchange.fetch_ticker(symbol)
            # 'last' is the most recent trade price
            prices[asset] = ticker['last']
            print(f"  {symbol}: ${ticker['last']:,.4f}")
        except ccxt.BadSymbol:
            print(f"  Warning: {symbol} not found on Binance, using fallback price.")
            prices[asset] = FALLBACK_PRICES.get(asset, 0.0)
        except (ccxt.NetworkError, ccxt.ExchangeError) as e:
            print(f"  Warning: Could not fetch {symbol}: {e}")
            prices[asset] = FALLBACK_PRICES.get(asset, 0.0)

    return prices


def build_portfolio_df(portfolio: dict, prices: dict) -> pd.DataFrame:
    """
    Build a detailed portfolio DataFrame with P&L calculations.

    Parameters
    ----------
    portfolio : dict of {symbol: {amount, avg_buy_price}}
    prices    : dict of {symbol: current_price}

    Returns
    -------
    pd.DataFrame with columns: asset, amount, avg_buy_price, current_price,
                                cost_basis, current_value, pnl_usd, pnl_pct
    """
    rows = []
    for asset, info in portfolio.items():
        amount        = info['amount']
        avg_buy       = info['avg_buy_price']
        current_price = prices.get(asset, 0.0)

        cost_basis    = amount * avg_buy
        current_value = amount * current_price
        pnl_usd       = current_value - cost_basis
        pnl_pct       = (pnl_usd / cost_basis) * 100 if cost_basis > 0 else 0.0

        rows.append({
            'Asset':         asset,
            'Amount':        amount,
            'Avg Buy Price': avg_buy,
            'Current Price': current_price,
            'Cost Basis':    cost_basis,
            'Current Value': current_value,
            'P&L ($)':       pnl_usd,
            'P&L (%)':       pnl_pct,
        })

    df = pd.DataFrame(rows)
    return df


def print_portfolio_table(df: pd.DataFrame) -> None:
    """Print the portfolio DataFrame in a formatted, human-readable table."""
    total_value  = df['Current Value'].sum()
    total_cost   = df['Cost Basis'].sum()
    total_pnl    = df['P&L ($)'].sum()
    total_pnl_pct = (total_pnl / total_cost) * 100 if total_cost > 0 else 0.0

    print("\n" + "=" * 85)
    print("  CRYPTO PORTFOLIO TRACKER")
    print("=" * 85)

    # Header
    header = f"  {'Asset':<6} {'Amount':>12} {'Avg Buy':>12} {'Current':>12} {'Value':>12} {'P&L $':>12} {'P&L %':>8}"
    print(header)
    print("  " + "-" * 81)

    for _, row in df.iterrows():
        pnl_sign = "+" if row['P&L ($)'] >= 0 else ""
        line = (
            f"  {row['Asset']:<6} "
            f"{row['Amount']:>12,.4f} "
            f"${row['Avg Buy Price']:>11,.2f} "
            f"${row['Current Price']:>11,.2f} "
            f"${row['Current Value']:>11,.2f} "
            f"{pnl_sign}${row['P&L ($)']:>10,.2f} "
            f"{pnl_sign}{row['P&L (%)']:>6.2f}%"
        )
        print(line)

    print("  " + "-" * 81)
    total_sign = "+" if total_pnl >= 0 else ""
    print(f"  {'TOTAL':<6} {'':>12} {'':>12} {'':>12} ${total_value:>11,.2f} "
          f"{total_sign}${total_pnl:>10,.2f} {total_sign}{total_pnl_pct:>6.2f}%")
    print("=" * 85)
    print(f"\n  Total Portfolio Value : ${total_value:,.2f}")
    print(f"  Total Cost Basis      : ${total_cost:,.2f}")
    print(f"  Unrealized P&L        : {total_sign}${total_pnl:,.2f}  ({total_sign}{total_pnl_pct:.2f}%)")
    print("=" * 85)


def plot_portfolio(df: pd.DataFrame, output_path: str) -> None:
    """
    Create a two-subplot figure:
      Left  — Pie chart showing portfolio allocation by current value
      Right — Bar chart showing P&L % per asset (green=profit, red=loss)

    Parameters
    ----------
    df          : Portfolio DataFrame
    output_path : Where to save the PNG
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

    # ---- Left: Pie Chart — Portfolio Allocation ----
    values = df['Current Value'].values
    labels = df['Asset'].values
    colors = plt.cm.Set3.colors[:len(labels)]  # type: ignore[attr-defined]

    wedges, texts, autotexts = ax1.pie(
        values,
        labels=labels,
        autopct='%1.1f%%',
        colors=colors,
        startangle=140,
        pctdistance=0.78,
        wedgeprops={'edgecolor': 'white', 'linewidth': 1.5}
    )
    for autotext in autotexts:
        autotext.set_fontsize(9)
        autotext.set_fontweight('bold')

    # Add dollar amounts to the legend
    legend_labels = [f"{row['Asset']} — ${row['Current Value']:,.0f}" for _, row in df.iterrows()]
    ax1.legend(wedges, legend_labels, loc='lower center', bbox_to_anchor=(0.5, -0.12),
               fontsize=9, ncol=2)

    total_value = df['Current Value'].sum()
    ax1.set_title(f'Portfolio Allocation\nTotal: ${total_value:,.0f}',
                  fontsize=13, fontweight='bold', pad=15)

    # ---- Right: Bar Chart — P&L % per Asset ----
    pnl_pct = df['P&L (%)'].values
    assets  = df['Asset'].values
    bar_colors = ['limegreen' if p >= 0 else 'tomato' for p in pnl_pct]

    bars = ax2.bar(assets, pnl_pct, color=bar_colors, edgecolor='white', linewidth=0.8)

    # Add value labels on top of each bar
    for bar, pct in zip(bars, pnl_pct):
        sign = '+' if pct >= 0 else ''
        y_pos = pct + (0.5 if pct >= 0 else -1.2)
        ax2.text(bar.get_x() + bar.get_width() / 2, y_pos,
                 f'{sign}{pct:.1f}%', ha='center', va='bottom', fontsize=9, fontweight='bold')

    ax2.axhline(y=0, color='black', linewidth=0.8, linestyle='-')
    ax2.set_title('Unrealized P&L by Asset (%)', fontsize=13, fontweight='bold', pad=15)
    ax2.set_ylabel('P&L (%)', fontsize=11)
    ax2.set_xlabel('Asset', fontsize=11)
    ax2.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{x:+.0f}%'))
    ax2.grid(True, axis='y', alpha=0.3, linestyle='--')
    ax2.tick_params(axis='x', labelsize=11)

    plt.suptitle('Crypto Portfolio Dashboard', fontsize=16, fontweight='bold', y=1.01)
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")


if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.abspath(__file__))
    chart_path = os.path.join(script_dir, 'portfolio_chart.png')

    assets = list(PORTFOLIO.keys())

    try:
        # Try to fetch live prices from Binance
        prices = fetch_live_prices(assets)
    except Exception as e:
        # If anything goes wrong, fall back to hardcoded prices
        print(f"[Warning] Could not fetch live prices ({e}), using fallback prices.")
        prices = FALLBACK_PRICES.copy()

    # Build the portfolio analysis table
    df = build_portfolio_df(PORTFOLIO, prices)

    # Print to console
    print_portfolio_table(df)

    # Generate charts
    try:
        plot_portfolio(df, chart_path)
    except Exception as e:
        print(f"[Warning] Could not generate chart: {e}")
        sys.exit(1)
