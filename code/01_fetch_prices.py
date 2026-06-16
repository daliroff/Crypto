"""
01_fetch_prices.py
==================
Fetch BTC/USDT OHLCV (candlestick) data from Binance using the ccxt library
and save it to a CSV file for use in subsequent lessons.

What is OHLCV?
--------------
OHLCV stands for Open, High, Low, Close, Volume — the standard format for
candlestick data used in technical analysis:
  - Open:   Price at the start of the time period
  - High:   Highest price reached during the period
  - Low:    Lowest price reached during the period
  - Close:  Price at the end of the period (most important for indicators)
  - Volume: Total amount of BTC traded during the period

Why Binance?
------------
Binance is the world's largest crypto exchange by volume. Its public REST API
requires no API key for historical market data, making it perfect for learning.
"""

import os
import ccxt
import pandas as pd


def fetch_btc_ohlcv(num_candles: int = 500) -> pd.DataFrame:
    """
    Connect to Binance and download BTC/USDT daily OHLCV candles.

    Parameters
    ----------
    num_candles : int
        Number of daily candles to fetch (max ~1000 for most exchanges).

    Returns
    -------
    pd.DataFrame
        DataFrame with columns: timestamp, open, high, low, close, volume
    """
    # --- Step 1: Create an exchange instance ---
    # ccxt supports 100+ exchanges with a unified API.
    # Setting 'enableRateLimit=True' automatically throttles requests to avoid
    # getting banned by the exchange's rate limiter.
    exchange = ccxt.binance({
        'enableRateLimit': True,  # Be a good citizen — respect API limits
    })

    print(f"Connected to: {exchange.name}")
    print(f"Fetching {num_candles} daily candles for BTC/USDT...")

    # --- Step 2: Fetch OHLCV data ---
    # Parameters:
    #   symbol   : The trading pair (base/quote currency)
    #   timeframe: '1d' = one day per candle. Others: '1m', '5m', '1h', '4h'
    #   since    : Start timestamp in milliseconds (None = most recent)
    #   limit    : Number of candles to return
    raw_ohlcv = exchange.fetch_ohlcv(
        symbol='BTC/USDT',
        timeframe='1d',
        since=None,       # Start from the most recent data and work backwards
        limit=num_candles
    )

    # raw_ohlcv is a list of lists: [[timestamp_ms, open, high, low, close, volume], ...]
    print(f"Received {len(raw_ohlcv)} candles from the exchange.")

    # --- Step 3: Convert to a pandas DataFrame ---
    # Using explicit column names makes the data self-documenting.
    df = pd.DataFrame(raw_ohlcv, columns=[
        'timestamp', 'open', 'high', 'low', 'close', 'volume'
    ])

    # --- Step 4: Convert timestamp from milliseconds to human-readable datetime ---
    # Exchanges return UNIX timestamps in milliseconds (ms) since Jan 1, 1970.
    # Example: 1609459200000 ms = 2021-01-01 00:00:00 UTC
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

    # Sort from oldest to newest (some exchanges return newest first)
    df = df.sort_values('timestamp').reset_index(drop=True)

    return df


def save_to_csv(df: pd.DataFrame, filename: str = 'btc_usdt_daily.csv') -> str:
    """
    Save the DataFrame to a CSV file in the same directory as this script.

    Parameters
    ----------
    df       : The OHLCV DataFrame to save
    filename : Output filename

    Returns
    -------
    str : Full path where the file was saved
    """
    # Build an absolute path so the file lands next to this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, filename)

    # index=False prevents pandas from writing the row numbers as a column
    df.to_csv(output_path, index=False)
    return output_path


def print_summary(df: pd.DataFrame) -> None:
    """Print a human-readable summary of the fetched data."""
    print("\n" + "=" * 50)
    print("DATA SUMMARY")
    print("=" * 50)
    print(f"  Date range : {df['timestamp'].iloc[0].date()} → {df['timestamp'].iloc[-1].date()}")
    print(f"  Candles    : {len(df)}")
    print(f"  Close range: ${df['close'].min():,.2f} – ${df['close'].max():,.2f}")
    print("\nFirst row:")
    print(df.iloc[0].to_string())
    print("\nLast row:")
    print(df.iloc[-1].to_string())
    print("=" * 50)


if __name__ == '__main__':
    try:
        # Fetch the data
        df = fetch_btc_ohlcv(num_candles=500)

        # Save it to CSV
        saved_path = save_to_csv(df)
        print(f"\nData saved to: {saved_path}")

        # Show a summary
        print_summary(df)

    except ccxt.NetworkError as e:
        # Raised when there is no internet connection or the exchange is unreachable
        print(f"[Network Error] Could not reach Binance: {e}")
        print("Check your internet connection and try again.")

    except ccxt.ExchangeError as e:
        # Raised for exchange-specific errors (e.g., invalid symbol, rate limit)
        print(f"[Exchange Error] Binance returned an error: {e}")

    except Exception as e:
        # Catch-all for unexpected errors
        print(f"[Unexpected Error] {type(e).__name__}: {e}")
