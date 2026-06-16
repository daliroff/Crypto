"""
04_macd_indicator.py
====================
Compute and visualize the MACD (Moving Average Convergence Divergence) indicator.

What is MACD?
-------------
MACD was developed by Gerald Appel in the late 1970s. It is a trend-following
momentum indicator that shows the relationship between two exponential moving
averages of a security's price.

MACD Components:
----------------
  1. MACD Line (fast):
       MACD = EMA(12) − EMA(26)
       - Positive MACD → short-term momentum is stronger than long-term (bullish)
       - Negative MACD → short-term momentum is weaker than long-term (bearish)

  2. Signal Line (slow):
       Signal = EMA(9) applied to the MACD Line
       - Acts as a trigger for buy/sell signals

  3. Histogram:
       Histogram = MACD Line − Signal Line
       - Visualizes the distance between MACD and Signal
       - Positive bars (above zero) → bullish momentum
       - Negative bars (below zero) → bearish momentum
       - Shrinking bars → momentum may be reversing

Trading Signals:
----------------
  BULLISH CROSSOVER: MACD Line crosses ABOVE Signal Line → buy signal
  BEARISH CROSSOVER: MACD Line crosses BELOW Signal Line → sell signal
  ZERO LINE CROSS:   MACD crosses above 0 → trend turning bullish
  DIVERGENCE:        Price makes new high but MACD does not → potential reversal

Parameters:
-----------
  (12, 26, 9) are the standard defaults used by most charting platforms.
  Short-term traders sometimes use (5, 35, 5) for more sensitivity.
"""

import os
import sys
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


def compute_macd(
    series: pd.Series,
    fast: int = 12,
    slow: int = 26,
    signal: int = 9
) -> pd.DataFrame:
    """
    Calculate the MACD indicator.

    Parameters
    ----------
    series : pd.Series
        Series of closing prices.
    fast   : int
        Fast EMA period (default 12).
    slow   : int
        Slow EMA period (default 26).
    signal : int
        Signal line EMA period (default 9).

    Returns
    -------
    pd.DataFrame with columns: macd_line, signal_line, histogram
    """
    # --- EMA calculations ---
    # adjust=False uses the recursive (standard) EMA formula
    ema_fast = series.ewm(span=fast,   adjust=False).mean()
    ema_slow = series.ewm(span=slow,   adjust=False).mean()

    # MACD Line: the difference between the two EMAs
    macd_line = ema_fast - ema_slow

    # Signal Line: EMA of the MACD Line (smoothed trigger)
    signal_line = macd_line.ewm(span=signal, adjust=False).mean()

    # Histogram: momentum between MACD and its signal
    histogram = macd_line - signal_line

    return pd.DataFrame({
        'macd_line':   macd_line,
        'signal_line': signal_line,
        'histogram':   histogram,
    })


def plot_macd(
    df: pd.DataFrame,
    fast: int = 12,
    slow: int = 26,
    signal: int = 9,
    output_path: str = 'macd_chart.png'
) -> None:
    """
    Create a two-panel chart: price on top, MACD components on bottom.

    Parameters
    ----------
    df          : DataFrame with 'close', 'macd_line', 'signal_line', 'histogram'
    fast        : Fast EMA period (for labeling)
    slow        : Slow EMA period (for labeling)
    signal      : Signal line period (for labeling)
    output_path : PNG output file path
    """
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 9),
                                    gridspec_kw={'height_ratios': [2, 1]},
                                    sharex=True)

    # ---- Panel 1: BTC Price ----
    ax1.plot(df.index, df['close'], color='steelblue', linewidth=1.5, label='BTC/USDT')
    ax1.set_title(f'BTC/USDT — Price and MACD({fast},{slow},{signal})',
                  fontsize=15, fontweight='bold', pad=12)
    ax1.set_ylabel('Price (USDT)', fontsize=12)
    ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${x:,.0f}'))
    ax1.legend(fontsize=11)
    ax1.grid(True, alpha=0.3, linestyle='--')

    # ---- Panel 2: MACD ----
    # MACD Line
    ax2.plot(df.index, df['macd_line'], color='steelblue', linewidth=1.5,
             label=f'MACD Line (EMA{fast} - EMA{slow})')

    # Signal Line
    ax2.plot(df.index, df['signal_line'], color='darkorange', linewidth=1.5,
             label=f'Signal Line (EMA{signal} of MACD)')

    # Histogram: color each bar individually based on sign
    # Positive bars (bullish momentum) = green; Negative bars = red
    hist = df['histogram']
    colors = ['limegreen' if v >= 0 else 'tomato' for v in hist]
    ax2.bar(df.index, hist, color=colors, alpha=0.6, width=1.0,
            label='Histogram (MACD − Signal)')

    # Zero line reference
    ax2.axhline(y=0, color='black', linestyle='--', linewidth=0.8, alpha=0.7)

    ax2.set_ylabel('MACD', fontsize=12)
    ax2.set_xlabel('Date', fontsize=12)
    ax2.legend(fontsize=10, loc='upper left')
    ax2.grid(True, alpha=0.3, linestyle='--')

    # Format shared x-axis dates
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    ax2.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
    fig.autofmt_xdate(rotation=30)

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")


def find_last_crossover(df: pd.DataFrame) -> None:
    """
    Detect and print the most recent MACD crossover signal.

    A crossover occurs when the MACD Line crosses the Signal Line.
    We detect this by checking where the sign of (macd - signal) changes.
    """
    # Sign of histogram: +1 when MACD > Signal, -1 when MACD < Signal
    sign = df['histogram'].apply(lambda x: 1 if x >= 0 else -1)

    # A crossover is where the sign flips (previous sign != current sign)
    crossovers = sign[sign != sign.shift(1)].dropna()

    if crossovers.empty:
        print("No MACD crossovers found in the dataset.")
        return

    # Most recent crossover
    last_cross_date = crossovers.index[-1]
    last_cross_type = crossovers.iloc[-1]
    price_at_cross  = df.loc[last_cross_date, 'close']
    macd_at_cross   = df.loc[last_cross_date, 'macd_line']

    print("\n" + "=" * 55)
    print("MACD CROSSOVER SIGNAL")
    print("=" * 55)
    print(f"  Most recent crossover: {last_cross_date.date()}")
    if last_cross_type == 1:
        print("  Type   : BULLISH — MACD Line crossed ABOVE Signal Line")
        print("  Signal : BUY / Look for long opportunities")
    else:
        print("  Type   : BEARISH — MACD Line crossed BELOW Signal Line")
        print("  Signal : SELL / Look for short opportunities")
    print(f"  Price at crossover : ${price_at_cross:,.2f}")
    print(f"  MACD at crossover  : {macd_at_cross:.2f}")

    # Show current MACD state
    latest = df.dropna(subset=['macd_line', 'signal_line']).iloc[-1]
    print(f"\n  Current MACD Line   : {latest['macd_line']:.2f}")
    print(f"  Current Signal Line : {latest['signal_line']:.2f}")
    print(f"  Current Histogram   : {latest['histogram']:.2f}")

    if latest['macd_line'] > latest['signal_line']:
        print("  Current State: MACD above Signal → Bullish bias")
    else:
        print("  Current State: MACD below Signal → Bearish bias")
    print("=" * 55)


if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path   = os.path.join(script_dir, 'btc_usdt_daily.csv')
    chart_path = os.path.join(script_dir, 'macd_chart.png')

    try:
        df = load_data(csv_path)

        # Compute MACD and merge results back into main DataFrame
        macd_df = compute_macd(df['close'], fast=12, slow=26, signal=9)
        df = pd.concat([df, macd_df], axis=1)

        plot_macd(df, fast=12, slow=26, signal=9, output_path=chart_path)
        find_last_crossover(df)

    except FileNotFoundError as e:
        print(f"[Error] {e}")
        sys.exit(1)

    except Exception as e:
        print(f"[Unexpected Error] {type(e).__name__}: {e}")
        sys.exit(1)
