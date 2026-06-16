"""
04_macd_indicator.py
====================
Compute and visualize the MACD (Moving Average Convergence Divergence) indicator.

What is MACD?
-------------
Developed by Gerald Appel (1979), MACD is a trend-following momentum indicator
built from the difference between two EMAs.

Components
----------
  fast_ema   = EMA(12) of closing price
  slow_ema   = EMA(26) of closing price
  macd_line  = fast_ema - slow_ema       ← main indicator line
  signal     = EMA(9) of macd_line       ← trigger line for entries/exits
  histogram  = macd_line - signal        ← visualizes distance between the two

How to read it
--------------
  MACD crosses ABOVE signal  → bullish signal (momentum turning up)
  MACD crosses BELOW signal  → bearish signal (momentum turning down)
  Histogram above 0          → bulls in control
  Histogram below 0          → bears in control
"""

import os
import sys
import numpy as np
import ccxt
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


CSV_FILE    = 'btc_ohlcv.csv'
OUTPUT_FILE = 'macd.png'


def load_or_fetch(script_dir: str) -> pd.DataFrame:
    """Return OHLCV DataFrame, loading from CSV if it exists, else fetching from Binance."""
    csv_path = os.path.join(script_dir, CSV_FILE)

    if os.path.exists(csv_path):
        print(f"Loading data from {csv_path}")
        df = pd.read_csv(csv_path, parse_dates=['timestamp'])
    else:
        print("CSV not found — fetching from Binance...")
        exchange = ccxt.binance({'enableRateLimit': True})
        raw = exchange.fetch_ohlcv('BTC/USDT', timeframe='1d', since=None, limit=365)
        df = pd.DataFrame(raw, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        df.to_csv(csv_path, index=False)
        print(f"Saved {len(df)} rows to {csv_path}")

    df = df.sort_values('timestamp').reset_index(drop=True)
    df = df.set_index('timestamp')
    print(f"Loaded {len(df)} rows  ({df.index[0].date()} → {df.index[-1].date()})")
    return df


def compute_macd(df: pd.DataFrame,
                 fast: int = 12,
                 slow: int = 26,
                 signal_period: int = 9) -> pd.DataFrame:
    """
    Add MACD columns to the DataFrame.

    Parameters
    ----------
    df            : DataFrame with a 'close' column
    fast          : Fast EMA period (default 12)
    slow          : Slow EMA period (default 26)
    signal_period : Signal line EMA period (default 9)
    """
    df['fast_ema']  = df['close'].ewm(span=fast,          adjust=False).mean()
    df['slow_ema']  = df['close'].ewm(span=slow,          adjust=False).mean()
    df['macd']      = df['fast_ema'] - df['slow_ema']
    df['signal']    = df['macd'].ewm(span=signal_period,  adjust=False).mean()
    df['histogram'] = df['macd'] - df['signal']
    return df


def plot_macd(df: pd.DataFrame, output_path: str) -> None:
    """
    Two-panel chart:
      Top    — BTC/USDT closing price
      Bottom — MACD line, signal line, and histogram bars
    """
    fig, (ax1, ax2) = plt.subplots(
        2, 1, figsize=(14, 9),
        gridspec_kw={'height_ratios': [2, 1]},
        sharex=True
    )

    # ---- Top panel: price ----
    ax1.plot(df.index, df['close'], color='steelblue', linewidth=1.5, label='BTC/USDT Close')
    ax1.set_title('BTC/USDT — Price and MACD(12, 26, 9)', fontsize=14, fontweight='bold', pad=12)
    ax1.set_ylabel('Price (USDT)', fontsize=12)
    ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${x:,.0f}'))
    ax1.legend(fontsize=11)
    ax1.grid(True, alpha=0.3, linestyle='--')

    # ---- Bottom panel: MACD ----
    ax2.plot(df.index, df['macd'],   color='steelblue',  linewidth=1.5, label='MACD Line')
    ax2.plot(df.index, df['signal'], color='darkorange',  linewidth=1.5, label='Signal Line')

    # Histogram: green bars when positive (bullish), red when negative (bearish)
    colors = np.where(df['histogram'] >= 0, 'green', 'red')
    ax2.bar(df.index, df['histogram'], color=colors, alpha=0.6, width=0.8, label='Histogram')

    ax2.axhline(0, color='black', linewidth=0.8, alpha=0.5)
    ax2.set_ylabel('MACD', fontsize=12)
    ax2.set_xlabel('Date', fontsize=12)
    ax2.legend(fontsize=10, loc='upper left')
    ax2.grid(True, alpha=0.3, linestyle='--')

    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    ax2.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
    fig.autofmt_xdate(rotation=30)

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")


if __name__ == '__main__':
    script_dir  = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, OUTPUT_FILE)

    try:
        df = load_or_fetch(script_dir)
        df = compute_macd(df, fast=12, slow=26, signal_period=9)

        last = df.dropna(subset=['macd', 'signal']).iloc[-1]
        print(f"\nLatest MACD   : {last['macd']:.2f}")
        print(f"Latest Signal : {last['signal']:.2f}")
        print(f"Histogram     : {last['histogram']:.2f}  "
              f"({'Bullish' if last['histogram'] >= 0 else 'Bearish'})")

        plot_macd(df, output_path)

    except ccxt.NetworkError as e:
        print(f"[Network Error] {e}")
        sys.exit(1)
    except Exception as e:
        print(f"[{type(e).__name__}] {e}")
        sys.exit(1)
