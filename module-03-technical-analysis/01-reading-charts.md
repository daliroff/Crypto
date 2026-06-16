# Lesson 01: Reading Charts

## Module 3 — Technical Analysis | Crypto Trading: Zero to Hero

---

## Introduction

Before you can trade crypto effectively, you need to speak the language of charts. Charts are the primary tool traders use to visualize price history, identify patterns, and make decisions. This lesson covers everything you need to understand what you're looking at when you open a chart on TradingView or any exchange.

---

## OHLCV Data: The Building Blocks of Every Chart

Every candlestick or bar on a chart is built from five data points, collectively called **OHLCV**:

- **Open (O):** The price at which the asset started trading during that time period. If you're on a 1-hour chart and it's the 3:00 PM candle, the Open is the price BTC traded at exactly 3:00 PM.
- **High (H):** The highest price reached during that period. This becomes the top of the upper wick on a candlestick.
- **Low (L):** The lowest price reached during that period. This becomes the bottom of the lower wick.
- **Close (C):** The final price at the end of the time period. This is often considered the most important data point — it represents the market's "verdict" for that candle.
- **Volume (V):** The total number of coins/tokens traded during that period. Volume is displayed as bars at the bottom of the chart.

For example, a daily BTC candle might show: Open $42,000 / High $43,500 / Low $41,200 / Close $43,100 / Volume 28,000 BTC. This tells you the market opened, sold off briefly, then pushed significantly higher and closed strong.

---

## Timeframes: Choosing the Right Lens

Timeframes determine how much price data is compressed into each candle. Each has a specific use:

### Short-Term Timeframes
- **1-minute (1m):** Used by scalpers. Extremely noisy — full of random fluctuations. Not recommended for beginners.
- **5-minute (5m):** Slightly less noise. Useful for timing entries on intraday moves.
- **15-minute (15m):** Popular with day traders for confirming short-term signals.

### Medium-Term Timeframes
- **1-hour (1h):** A strong balance between detail and signal quality. One of the most widely used timeframes.
- **4-hour (4h):** Excellent for swing traders. Shows multi-day trends clearly. Many professional traders rely on this timeframe heavily.

### Long-Term Timeframes
- **Daily (1D):** The benchmark timeframe. Shows how BTC or ETH has moved day-by-day. Great for identifying major trends.
- **Weekly (1W):** The big picture. Each candle represents a full week. Used to identify macro bull and bear markets.

**Rule of thumb:** Always start your analysis on higher timeframes (1D or 4h) before dropping to lower timeframes for entry timing. Trading with the higher timeframe trend dramatically improves win rates.

---

## Chart Types: Line, Bar, and Candlestick

### Line Charts
A line chart connects only the **closing prices** of each period. Simple and clean, but strips out a huge amount of information — no highs, lows, or opens. Useful for a quick glance at the overall direction, but insufficient for serious trading.

### Bar Charts (OHLC Bars)
Bar charts show Open, High, Low, and Close. The vertical bar represents the high-to-low range; horizontal notches show the open (left) and close (right). All the data is there, but they're harder to read quickly.

### Candlestick Charts
**Candlestick charts** are the industry standard for crypto trading. They display OHLCV data in a visually intuitive way:
- A wide body shows the range between the open and close.
- **Green (bullish) candle:** Close is higher than Open — buyers won the period.
- **Red (bearish) candle:** Close is lower than Open — sellers won the period.
- Thin lines above and below the body (called **wicks** or **shadows**) show the high and low.

Candlesticks make it easy to see at a glance whether bulls or bears are in control.

---

## Reading Price Action: Trend and Volatility

**Trend direction** is the most fundamental concept in technical analysis:
- **Uptrend:** Higher highs and higher lows. Each peak surpasses the last; each pullback holds above the previous pullback low.
- **Downtrend:** Lower highs and lower lows. Each rally fails below the previous peak.
- **Sideways / Ranging:** Price bounces between a defined ceiling (resistance) and floor (support) without establishing a clear directional bias.

**Volatility** refers to how much price moves in a given period. On a BTC chart, tight clusters of small candles indicate low volatility (compression), while large candles with long wicks indicate high volatility. Low-volatility periods often precede explosive moves — traders watch for these "coiling" patterns.

---

## TradingView: Setting Up Your Chart

**TradingView** (tradingview.com) is the most popular charting platform in crypto. Here's how to get started:

1. Create a free account at tradingview.com
2. Click "Chart" in the top navigation
3. In the search bar (top left), type the symbol you want: `BTCUSDT`, `ETHUSDT`, `SOLUSDT`
4. Select the exchange (Binance, Coinbase, Kraken, etc.)
5. Choose your timeframe using the toolbar at the top: 1, 5, 15, 60 (1h), 240 (4h), D, W
6. Switch to **Candlestick** view using the chart type dropdown
7. Right-click the chart to access settings, or use the toolbar to add indicators

Pro tip: Save your chart layouts. Once you've set up your preferred indicators and style, save the layout so you don't have to rebuild it every session.

---

## Zooming Out: The Importance of Higher Timeframe Context

One of the biggest mistakes beginners make is trading only on low timeframes without checking the bigger picture. A bullish pattern on the 15-minute chart means very little if the daily chart shows a strong downtrend.

**Always ask:** What is the daily chart saying? What is the weekly chart saying? If you're looking to buy ETH based on a 1h signal, but the weekly chart shows ETH in a confirmed downtrend, the probability of that trade succeeding is much lower.

This concept is called **top-down analysis**: start high, work low.

---

## Reading Volume Bars

Volume bars appear at the bottom of most charts. Each bar corresponds to a candle above it, showing how much of the asset traded during that period.

- **High volume = conviction.** When a big price move happens on high volume, it means many participants agreed on that direction. The move is more likely to continue.
- **Low volume = uncertainty.** A price move on thin volume may be easily reversed.
- **Volume spikes** often occur at major turning points — climactic selling at bottoms, or explosive buying at breakouts.
- Color-coded volume bars (green when price went up, red when it went down) make it easy to see whether buyers or sellers were more active.

---

## Price Scales: Linear vs. Logarithmic

Most charts default to a **linear scale**, where equal vertical distances represent equal dollar amounts. This works fine for short timeframes.

However, for long-term crypto charts, a **logarithmic (log) scale** is far more informative. On a log scale, equal vertical distances represent equal **percentage** moves. This matters because:

- BTC moving from $1,000 to $2,000 (100% gain) looks the same size as $50,000 to $100,000 (also 100%) on a log chart.
- On a linear chart, the $1,000 → $2,000 move looks insignificant compared to the $50,000 → $100,000 move, even though they're the same percentage gain.
- Long-term trendlines on BTC's weekly chart are far more accurate when drawn on a log scale.

**Always use log scale when analyzing long-term crypto price history.**

To switch in TradingView: right-click on the price axis → "Log Scale."

---

## Key Takeaways

> **Lesson 01 — Reading Charts**
>
> - **OHLCV** (Open, High, Low, Close, Volume) is the raw data behind every candle. Learn what each component means.
> - **Timeframes** range from 1-minute (noise) to weekly (macro trend). Always analyze top-down — start with higher timeframes before zooming in.
> - **Candlestick charts** are the standard for crypto trading. Green = bullish candle (close > open), Red = bearish (close < open).
> - **Trend direction** is defined by higher highs/higher lows (uptrend) or lower highs/lower lows (downtrend).
> - **TradingView** is the go-to charting tool. Set it up with your preferred pairs and timeframes early.
> - **Volume confirms price moves.** High volume moves are more reliable than low volume moves.
> - **Use logarithmic scale** for long-term crypto charts to see percentage-based moves accurately.
> - Never trade only on a low timeframe without checking what the daily and weekly charts are showing.
