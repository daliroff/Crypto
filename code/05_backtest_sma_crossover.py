"""
05_backtest_sma_crossover.py
============================
Full backtesting of the classic SMA Crossover strategy on BTC/USDT daily data.

What is Backtesting?
--------------------
Backtesting applies a trading strategy to historical data to simulate how it
would have performed. While past performance never guarantees future results,
backtesting helps you:
  - Understand the strategy's behavior
  - Measure risk (drawdown, volatility)
  - Compare against a simple buy-and-hold baseline

SMA Crossover Strategy:
-----------------------
  Rule: When the fast SMA (20-day) crosses ABOVE the slow SMA (50-day),
        go LONG (buy). When it crosses BELOW, EXIT (sell/flat).

  Why it works (in theory):
    - A rising SMA20 faster than SMA50 signals increasing short-term momentum
    - Classic "trend following" — ride the trend, exit when it reverses

Important: Look-Ahead Bias
--------------------------
  A critical mistake in backtesting is using the signal on the SAME day it
  forms. In practice, you act on tomorrow's open after today's signal close.
  We prevent this by using position = signal.shift(1) — the signal is delayed
  by one period before being applied to returns.

Performance Metrics Explained:
-------------------------------
  Total Return     : (final_value / initial_value - 1) * 100
  Annualized Return: ((1 + total_return)^(252/n_days) - 1) * 100
  Sharpe Ratio     : mean(daily_ret) / std(daily_ret) * sqrt(252)
                     Measures return per unit of risk (>1 = good, >2 = great)
  Max Drawdown     : Largest peak-to-trough decline in portfolio value
  Win Rate         : % of trades that were profitable
  Profit Factor    : Total profit / Total loss (>1 = profitable system)
"""

import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def load_data(filepath: str) -> pd.DataFrame:
    """Load OHLCV CSV and return a DatetimeIndex DataFrame."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(
            f"Data file not found: {filepath}\n"
            "Please run 01_fetch_prices.py first."
        )
    df = pd.read_csv(filepath, parse_dates=['timestamp'])
    df = df.set_index('timestamp').sort_index()
    print(f"Loaded {len(df)} rows.")
    return df


def generate_signals(df: pd.DataFrame, fast: int = 20, slow: int = 50) -> pd.DataFrame:
    """
    Compute SMA crossover signals with no look-ahead bias.

    Parameters
    ----------
    df   : DataFrame with 'close' column
    fast : Fast SMA period
    slow : Slow SMA period

    Returns
    -------
    DataFrame enriched with: sma_fast, sma_slow, signal, position
    """
    df = df.copy()

    # Calculate the two moving averages
    df['sma_fast'] = df['close'].rolling(window=fast).mean()
    df['sma_slow'] = df['close'].rolling(window=slow).mean()

    # Signal: 1 when fast MA is above slow MA (bullish), 0 otherwise
    # This is the "raw" signal on the day it forms
    df['signal'] = 0
    df.loc[df['sma_fast'] > df['sma_slow'], 'signal'] = 1

    # Position: shift by 1 to avoid look-ahead bias
    # We act on the NEXT day's open, not the same candle that generated the signal
    df['position'] = df['signal'].shift(1)

    return df


def calculate_returns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate strategy and buy-and-hold returns.

    Parameters
    ----------
    df : DataFrame with 'close' and 'position' columns

    Returns
    -------
    DataFrame with daily_return, strategy_return, cum_strategy, cum_bh columns
    """
    df = df.copy()

    # Daily percentage return of the asset itself
    df['daily_return'] = df['close'].pct_change()

    # Strategy return: apply position (0 or 1) to the daily return
    # If position=1 (long), we capture the move. If 0, we earn nothing.
    df['strategy_return'] = df['daily_return'] * df['position']

    # Cumulative returns: (1 + r1) * (1 + r2) * ... - 1
    df['cum_strategy'] = (1 + df['strategy_return']).cumprod()
    df['cum_bh']       = (1 + df['daily_return']).cumprod()

    return df


def compute_drawdown(cum_returns: pd.Series) -> pd.Series:
    """
    Compute the running drawdown (as a fraction) from the cumulative returns series.

    Drawdown at time t = (peak_up_to_t - value_at_t) / peak_up_to_t
    """
    # Running maximum (highest portfolio value seen so far)
    running_max = cum_returns.cummax()

    # Drawdown = how far below the peak we are, as a percentage
    drawdown = (cum_returns - running_max) / running_max
    return drawdown


def compute_performance_metrics(df: pd.DataFrame) -> dict:
    """
    Compute a comprehensive set of performance statistics.

    Parameters
    ----------
    df : DataFrame with strategy_return, daily_return, cum_strategy, cum_bh columns

    Returns
    -------
    dict of metrics
    """
    # Drop NaN rows (early rows before SMA windows are filled)
    strat = df['strategy_return'].dropna()
    bh    = df['daily_return'].dropna()

    # --- Returns ---
    total_return    = df['cum_strategy'].iloc[-1] - 1
    bh_return       = df['cum_bh'].iloc[-1] - 1

    # Annualized return: convert total return over n trading days to annualized
    n_days = len(strat)
    annualized_return = (1 + total_return) ** (252 / n_days) - 1

    # --- Risk ---
    # Sharpe ratio: annualized mean return divided by annualized volatility
    # Assumes risk-free rate ≈ 0 (reasonable simplification for crypto)
    sharpe = (strat.mean() / strat.std()) * np.sqrt(252) if strat.std() > 0 else 0.0

    # Max drawdown
    drawdown    = compute_drawdown(df['cum_strategy'].dropna())
    max_drawdown = drawdown.min()

    # --- Trade analysis ---
    # Identify individual trade returns by looking at stretches where position=1
    position = df['position'].fillna(0)

    # Mark the first day of each trade (position goes from 0 to 1)
    trade_starts = (position == 1) & (position.shift(1) == 0)
    trade_ends   = (position == 0) & (position.shift(1) == 1)

    # Calculate return for each trade period
    trade_returns = []
    entry_idx = None
    for i, (idx, row) in enumerate(df.iterrows()):
        if trade_starts.loc[idx]:
            entry_idx = idx
        if trade_ends.loc[idx] and entry_idx is not None:
            # Return from entry to exit using cumulative strategy returns
            try:
                entry_val = df.loc[entry_idx, 'cum_strategy']
                exit_val  = df.loc[idx, 'cum_strategy']
                trade_returns.append(exit_val / entry_val - 1)
            except Exception:
                pass
            entry_idx = None

    num_trades  = len(trade_returns)
    win_rate    = (sum(1 for r in trade_returns if r > 0) / num_trades * 100) if num_trades > 0 else 0

    wins   = [r for r in trade_returns if r > 0]
    losses = [abs(r) for r in trade_returns if r < 0]
    profit_factor = (sum(wins) / sum(losses)) if losses else float('inf')

    return {
        'total_return':       total_return * 100,
        'bh_return':          bh_return * 100,
        'annualized_return':  annualized_return * 100,
        'sharpe_ratio':       sharpe,
        'max_drawdown':       max_drawdown * 100,
        'win_rate':           win_rate,
        'num_trades':         num_trades,
        'profit_factor':      profit_factor,
        'n_days':             n_days,
    }


def plot_backtest(
    df: pd.DataFrame,
    fast: int,
    slow: int,
    output_path: str
) -> None:
    """
    Create a 3-panel backtest chart:
      Panel 1 — Price with SMA lines and trade markers
      Panel 2 — Portfolio value (strategy vs buy-and-hold)
      Panel 3 — Drawdown
    """
    fig, axes = plt.subplots(3, 1, figsize=(14, 14),
                              gridspec_kw={'height_ratios': [2, 1.5, 1]},
                              sharex=True)
    ax1, ax2, ax3 = axes

    # ---- Panel 1: Price + SMA lines + signals ----
    ax1.plot(df.index, df['close'],    color='steelblue', linewidth=1.2, label='Close Price')
    ax1.plot(df.index, df['sma_fast'], color='darkorange', linewidth=1.8,
             linestyle='--', label=f'SMA({fast})')
    ax1.plot(df.index, df['sma_slow'], color='purple', linewidth=1.8,
             linestyle='--', label=f'SMA({slow})')

    # Mark buy signals: where fast crosses above slow (signal goes from 0→1)
    buy_signals = df[(df['signal'] == 1) & (df['signal'].shift(1) == 0)]
    ax1.scatter(buy_signals.index, buy_signals['close'],
                marker='^', color='lime', s=80, zorder=5, label='Buy Signal')

    # Mark sell signals: where fast crosses below slow (signal goes from 1→0)
    sell_signals = df[(df['signal'] == 0) & (df['signal'].shift(1) == 1)]
    ax1.scatter(sell_signals.index, sell_signals['close'],
                marker='v', color='red', s=80, zorder=5, label='Sell Signal')

    ax1.set_title(f'BTC/USDT — SMA({fast}/{slow}) Crossover Backtest',
                  fontsize=15, fontweight='bold', pad=12)
    ax1.set_ylabel('Price (USDT)', fontsize=11)
    ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${x:,.0f}'))
    ax1.legend(fontsize=10, loc='upper left')
    ax1.grid(True, alpha=0.3, linestyle='--')

    # ---- Panel 2: Portfolio value ----
    ax2.plot(df.index, df['cum_strategy'] * 100, color='limegreen', linewidth=2.0,
             label='SMA Crossover Strategy')
    ax2.plot(df.index, df['cum_bh'] * 100, color='steelblue', linewidth=2.0,
             linestyle='--', label='Buy and Hold')
    ax2.axhline(y=100, color='gray', linestyle=':', linewidth=0.8)
    ax2.set_ylabel('Portfolio Value\n(100 = starting capital)', fontsize=11)
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3, linestyle='--')

    # ---- Panel 3: Drawdown ----
    drawdown = compute_drawdown(df['cum_strategy'].dropna()) * 100
    ax3.fill_between(drawdown.index, drawdown, 0, color='tomato', alpha=0.5)
    ax3.plot(drawdown.index, drawdown, color='red', linewidth=1.0)
    ax3.set_ylabel('Drawdown (%)', fontsize=11)
    ax3.set_xlabel('Date', fontsize=11)
    ax3.grid(True, alpha=0.3, linestyle='--')

    # Format x-axis
    ax3.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    ax3.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
    fig.autofmt_xdate(rotation=30)

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")


def print_performance_report(metrics: dict, fast: int, slow: int) -> None:
    """Print a formatted performance report to the console."""
    print("\n" + "=" * 55)
    print(f"  BACKTEST REPORT — SMA({fast}/{slow}) Crossover")
    print("=" * 55)
    print(f"  Period Tested       : {metrics['n_days']} trading days")
    print(f"  Number of Trades    : {metrics['num_trades']}")
    print()
    print("  RETURNS:")
    print(f"    Strategy Total    : {metrics['total_return']:+.2f}%")
    print(f"    Buy-and-Hold      : {metrics['bh_return']:+.2f}%")
    print(f"    Annualized        : {metrics['annualized_return']:+.2f}%")
    print()
    print("  RISK:")
    print(f"    Sharpe Ratio      : {metrics['sharpe_ratio']:.2f}  (>1 = good)")
    print(f"    Max Drawdown      : {metrics['max_drawdown']:.2f}%")
    print()
    print("  TRADE QUALITY:")
    print(f"    Win Rate          : {metrics['win_rate']:.1f}%")
    print(f"    Profit Factor     : {metrics['profit_factor']:.2f}  (>1 = profitable)")
    print("=" * 55)
    print()

    # Verdict
    if metrics['total_return'] > metrics['bh_return']:
        print("  VERDICT: Strategy OUTPERFORMED buy-and-hold.")
    else:
        diff = metrics['bh_return'] - metrics['total_return']
        print(f"  VERDICT: Strategy underperformed buy-and-hold by {diff:.1f}%.")
        print("  Note: SMA crossover often lags in trending markets due to")
        print("  the inherent delay in moving averages ('whipsaw' effect).")
    print("=" * 55)


if __name__ == '__main__':
    FAST = 20
    SLOW = 50

    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path   = os.path.join(script_dir, 'btc_usdt_daily.csv')
    chart_path = os.path.join(script_dir, 'backtest_sma_crossover.png')

    try:
        df = load_data(csv_path)
        df = generate_signals(df, fast=FAST, slow=SLOW)
        df = calculate_returns(df)

        metrics = compute_performance_metrics(df)
        print_performance_report(metrics, fast=FAST, slow=SLOW)
        plot_backtest(df, fast=FAST, slow=SLOW, output_path=chart_path)

    except FileNotFoundError as e:
        print(f"[Error] {e}")
        sys.exit(1)

    except Exception as e:
        print(f"[Unexpected Error] {type(e).__name__}: {e}")
        sys.exit(1)
