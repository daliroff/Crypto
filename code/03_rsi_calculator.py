"""
03_rsi_calculator.py
====================
Compute and visualize the Relative Strength Index (RSI) for BTC/USDT daily data.

What is RSI?
------------
RSI is a momentum oscillator developed by J. Welles Wilder Jr. (1978).
It measures the speed and magnitude of recent price changes on a 0–100 scale:

  RSI > 70  → Overbought: asset may be overextended, watch for a pullback
  RSI < 30  → Oversold:   asset may be undervalued, watch for a bounce
  RSI ≈ 50  → Neutral:    no strong directional momentum

Wilder's smoothing method
--------------------------
1. delta_t = close_t - close_{t-1}
2. gain_t  = delta_t  if delta_t > 0 else 0
   loss_t  = |delta_t| if delta_t < 0 else 0
3. avg_gain = EWM(gain, alpha=1/14)   ← Wilder's EMA (alpha=1/period)
   avg_loss = EWM(loss, alpha=1/14)
4. RS = avg_gain / avg_loss
5. RSI = 100 - (100 / (1 + RS))
"""

import os
import sys
import numpy as np
import ccxt
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.collections import LineCollection
import matplotlib.colors as mcolors


CSV_FILE   = 'btc_ohlcv.csv'
OUTPUT_FILE = 'rsi.png'


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


def compute_rsi(series: pd.Series, period: int = 14) -> pd.Series:
    """
    Compute RSI using Wilder's smoothing (EWM with alpha=1/period, adjust=False).

    Parameters
    ----------
    series : pd.Series  — closing price series
    period : int        — look-back window (Wilder used 14)

    Returns
    -------
    pd.Series of RSI values in [0, 100]
    """
    delta  = series.diff()
    gains  = delta.clip(lower=0)
    losses = (-delta).clip(lower=0)

    alpha    = 1.0 / period
    avg_gain = gains.ewm(alpha=alpha, adjust=False).mean()
    avg_loss = losses.ewm(alpha=alpha, adjust=False).mean()

    # Avoid division by zero when avg_loss is 0 (pure uptrend)
    rs  = avg_gain / avg_loss.replace(0, np.finfo(float).eps)
    rsi = 100.0 - (100.0 / (1.0 + rs))
    return rsi


def plot_rsi(df: pd.DataFrame, period: int = 14, output_path: str = OUTPUT_FILE) -> None:
    """
    Two-panel chart: price (top) and RSI (bottom).
    RSI line is colored: red when >70, green when <30, blue otherwise.
    """
    rsi = df['rsi']

    fig, (ax1, ax2) = plt.subplots(
        2, 1, figsize=(14, 9),
        gridspec_kw={'height_ratios': [2, 1]},
        sharex=True
    )

    # ---- Top panel: price ----
    ax1.plot(df.index, df['close'], color='steelblue', linewidth=1.5, label='BTC/USDT Close')
    ax1.set_title('BTC/USDT — Price and RSI(14)', fontsize=14, fontweight='bold', pad=12)
    ax1.set_ylabel('Price (USDT)', fontsize=12)
    ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${x:,.0f}'))
    ax1.legend(fontsize=11)
    ax1.grid(True, alpha=0.3, linestyle='--')

    # ---- Bottom panel: RSI with segment coloring ----
    # Build colored line segments: red >70, green <30, blue otherwise
    x    = mdates.date2num(df.index.to_pydatetime())
    y    = rsi.values
    mask_ob = y > 70      # overbought
    mask_os = y < 30      # oversold

    # Draw three layers so the legend shows clean color entries
    ax2.plot(df.index, rsi, color='steelblue', linewidth=1.5, label=f'RSI({period})')
    # Overprint overbought segments in red
    ob_y = np.where(mask_ob, y, np.nan)
    ax2.plot(df.index, ob_y, color='red',   linewidth=2.0, label='Overbought (>70)')
    # Overprint oversold segments in green
    os_y = np.where(mask_os, y, np.nan)
    ax2.plot(df.index, os_y, color='green', linewidth=2.0, label='Oversold (<30)')

    # Reference lines
    ax2.axhline(70, color='red',   linestyle='--', linewidth=1.0, alpha=0.7)
    ax2.axhline(30, color='green', linestyle='--', linewidth=1.0, alpha=0.7)
    ax2.axhline(50, color='gray',  linestyle=':',  linewidth=0.8, alpha=0.5)

    # Shaded zones for readability
    ax2.fill_between(df.index, rsi, 70, where=(rsi >= 70), interpolate=True,
                     color='red',   alpha=0.15)
    ax2.fill_between(df.index, rsi, 30, where=(rsi <= 30), interpolate=True,
                     color='green', alpha=0.15)

    ax2.set_ylabel(f'RSI({period})', fontsize=12)
    ax2.set_xlabel('Date', fontsize=12)
    ax2.set_ylim(0, 100)
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
        df['rsi'] = compute_rsi(df['close'], period=14)

        current_rsi = df['rsi'].iloc[-1]
        print(f"\nLatest RSI(14): {current_rsi:.2f}  ", end='')
        if current_rsi > 70:
            print("→ OVERBOUGHT")
        elif current_rsi < 30:
            print("→ OVERSOLD")
        else:
            print("→ NEUTRAL")

        plot_rsi(df, period=14, output_path=output_path)

    except ccxt.NetworkError as e:
        print(f"[Network Error] {e}")
        sys.exit(1)
    except Exception as e:
        print(f"[{type(e).__name__}] {e}")
        sys.exit(1)
