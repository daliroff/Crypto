"""
02_moving_average.py
====================
Load BTC/USDT daily OHLCV data, compute four moving averages, and plot them.

Moving Averages at a glance
----------------------------
Simple Moving Average (SMA):
    SMA(n) = mean of the last n closing prices.
    Every period gets equal weight, so it reacts slowly to recent moves.

Exponential Moving Average (EMA):
    EMA gives progressively more weight to recent prices via a smoothing
    factor k = 2 / (span + 1).
    Formula: EMA_t = Close_t * k + EMA_{t-1} * (1 - k)
    Reacts faster than SMA — useful for catching trend changes early.

Common interpretations
-----------------------
  Price above MA      → bullish (price leading the average)
  Short MA > long MA  → uptrend
  Short MA < long MA  → downtrend / potential "death cross"
"""

import os
import sys
import ccxt
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


CSV_FILE = 'btc_ohlcv.csv'
OUTPUT_FILE = 'moving_averages.png'


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


def compute_moving_averages(df: pd.DataFrame) -> pd.DataFrame:
    """Add SMA(20), SMA(50), EMA(20), EMA(50) columns to the DataFrame."""
    df['sma20'] = df['close'].rolling(window=20).mean()
    df['sma50'] = df['close'].rolling(window=50).mean()
    # adjust=False uses the recursive EMA formula (standard industry convention)
    df['ema20'] = df['close'].ewm(span=20, adjust=False).mean()
    df['ema50'] = df['close'].ewm(span=50, adjust=False).mean()
    return df


def plot_moving_averages(df: pd.DataFrame, output_path: str) -> None:
    fig, ax = plt.subplots(figsize=(14, 6))

    ax.plot(df.index, df['close'], color='steelblue',  linewidth=1.4, label='BTC/USDT Close', alpha=0.9)
    ax.plot(df.index, df['sma20'], color='darkorange',  linewidth=1.8, linestyle='--', label='SMA(20)')
    ax.plot(df.index, df['sma50'], color='crimson',     linewidth=1.8, linestyle='--', label='SMA(50)')
    ax.plot(df.index, df['ema20'], color='limegreen',   linewidth=1.8, label='EMA(20)')
    ax.plot(df.index, df['ema50'], color='mediumpurple', linewidth=1.8, label='EMA(50)')

    ax.set_title('BTC/USDT — Price with SMA(20), SMA(50), EMA(20), EMA(50)',
                 fontsize=14, fontweight='bold', pad=12)
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Price (USDT)', fontsize=12)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${x:,.0f}'))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
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
        df = compute_moving_averages(df)
        plot_moving_averages(df, output_path)

    except ccxt.NetworkError as e:
        print(f"[Network Error] {e}")
        sys.exit(1)
    except Exception as e:
        print(f"[{type(e).__name__}] {e}")
        sys.exit(1)
