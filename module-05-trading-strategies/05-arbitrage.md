# Crypto Arbitrage

Arbitrage is the practice of simultaneously buying an asset in one market and selling it in another to profit from a price difference between the two. In theory, it is risk-free profit. In practice, the window between identifying an opportunity and executing on it is measured in milliseconds — and the competition to close that window is fierce. Understanding how arbitrage works, why price discrepancies exist, and why retail traders are largely shut out of it today is essential knowledge for any serious crypto market participant.

## Why Price Discrepancies Exist

In a perfectly efficient market, the same asset would trade at exactly the same price everywhere. Crypto markets are not perfectly efficient, and several structural factors create temporary price gaps:

- **Fragmented liquidity:** Hundreds of exchanges operate independently with their own order books. Unlike traditional equity markets with centralized clearing, crypto has no single price feed or settlement layer. Binance's BTC/USDT price and Kraken's BTC/USD price are set by entirely separate supply and demand.
- **Regional capital flows:** Exchanges serving different geographies experience different buying and selling pressure. South Korean exchanges historically traded at a persistent premium — known as the "Kimchi Premium" — due to local demand outstripping supply and capital controls preventing easy arbitrage.
- **Different quote currencies:** Price differences appear between BTC/USDT and BTC/USD markets, or between stablecoin variants (USDC vs USDT), creating indirect arbitrage opportunities.
- **Speed of information:** Large news events move some exchanges faster than others, creating brief windows before all markets reprice.

## Types of Crypto Arbitrage

### Exchange Arbitrage (Spatial Arbitrage)

The simplest form: the same asset trades at different prices on two exchanges. Buy low on Exchange A, sell high on Exchange B.

**Example:** ETH is priced at $1,980 on Binance and $2,010 on Kraken at the same moment. Buy 10 ETH on Binance for $19,800. Transfer to Kraken. Sell for $20,100. Gross profit: $300.

The problems emerge immediately in the execution chain: transfer fees, withdrawal limits, network confirmation times (even a 30-second ETH transfer is too slow for most arbitrage windows), and the near-certainty that by the time your transfer confirms, the price gap has closed.

### Triangular Arbitrage

Triangular arbitrage does not require moving funds between exchanges. It exploits pricing inconsistencies between three trading pairs on the same exchange.

**Example on a single exchange:**
- BTC/USDT: 1 BTC = $40,000
- ETH/USDT: 1 ETH = $2,000
- ETH/BTC: 1 ETH = 0.0510 BTC (this is the discrepancy — based on the above, it should be 0.0500)

The arbitrage path:
1. Start with $40,000 USDT
2. Buy 1 BTC at $40,000 → you have 1 BTC
3. Sell 1 BTC for ETH at 0.0510 BTC/ETH → you receive 19.6 ETH (1 / 0.0510)
4. Sell 19.6 ETH for USDT at $2,000/ETH → you receive $39,200

Wait — that is a loss. The direction of the arbitrage matters. Reverse it:
1. Start with $40,000 USDT
2. Buy ETH at $2,000 → you have 20 ETH
3. Sell 20 ETH for BTC at 0.0510 → you receive 1.02 BTC
4. Sell 1.02 BTC for USDT at $40,000 → you receive $40,800

Gross profit: $800 on $40,000 capital. The direction and timing must be correct, and the rates must be checked simultaneously — sequential quotes are already stale data.

### DeFi Arbitrage

Decentralized exchanges (DEXs) like Uniswap, Curve, and SushiSwap price assets using automated market makers (AMMs) rather than order books. AMM prices update only when trades occur, creating predictable lag relative to centralized exchange prices.

When a large trade happens on Binance that moves the ETH price, the Uniswap pool price does not update until an arbitrageur makes a trade that brings it back into alignment. This arbitrage is highly competitive and is dominated by MEV (Maximal Extractable Value) bots that:
- Monitor the mempool for pending large trades
- Front-run or back-run those trades to capture the arbitrage
- Execute through custom smart contracts in a single atomic transaction (all succeeds or all reverts)

Cross-DEX arbitrage (buying on Uniswap and selling on Curve in the same transaction) is also common. These are purely on-chain, no transfer delay — but again, bots dominate.

## Execution Speed Requirements

Exchange arbitrage has an extremely short half-life. Studies of major crypto exchange price divergences show that price gaps between tier-1 exchanges typically close within **5 to 30 seconds** during high-liquidity periods. In illiquid markets or during extreme events, gaps persist longer but carry higher risk.

To act within this window requires:
- Automated detection software scanning multiple exchange APIs simultaneously
- Pre-funded accounts on both exchanges (no transfer time)
- API-connected order placement, not manual trading
- Co-location or low-latency network connections for the most competitive strategies

A human trader manually checking prices on two browser tabs and entering orders cannot compete. By the time the order is placed, the gap is gone.

## Fees: The Profit Killer

Every leg of an arbitrage trade carries costs, and they compound:

| Cost Type | Typical Range |
|-----------|--------------|
| Taker fee (each exchange) | 0.05% – 0.10% |
| Withdrawal/transfer fee | Varies by asset ($0.50–$5 for ETH) |
| Network gas fees (for DeFi) | Variable, can spike sharply |
| Spread (bid-ask) | 0.01% – 0.5% depending on liquidity |
| Slippage on large orders | 0.1% – 2% |

For the Binance/Kraken ETH example with a $30 price difference on a $1,980 asset (1.5% gap):
- Taker fees on both sides: ~0.20% total = $39.60 on $19,800
- Network transfer fee for 10 ETH: ~$5
- Slippage on 10 ETH order: ~$20–$40 depending on depth

Suddenly the $300 gross profit is reduced to approximately $215–$235 net — and that assumes the gap had not closed during the transfer.

At smaller price gaps (0.3%–0.5%, which is more typical for major assets), fees consume the entire arbitrage profit.

## The Real ETH Price Discrepancy Example

On volatile trading days, ETH price differences between Binance and Kraken can briefly widen. A realistic scenario:

- A major market-moving news event hits at 14:23:07 UTC
- ETH on Binance drops instantly to $1,940 as market sell orders trigger
- ETH on Kraken lags at $1,970 for approximately 8 seconds before sellers catch up
- Price gap: $30 (1.5%)

**Could you profit?** Only if:
1. Your monitoring software detected the gap within 1–2 seconds
2. You had USDT pre-funded on Binance and ETH pre-funded on Kraken
3. You bought on Binance and sold on Kraken simultaneously via API
4. Your two orders filled without slippage destroying the margin

Realistically, you also faced the risk that the gap reflected genuine new price discovery — meaning Kraken would move down to $1,940, not Binance moving back up to $1,970. Buying the "cheap" asset can mean buying an asset in the process of correctly pricing bad news.

## Why Retail Arbitrage Is Nearly Impossible Today

The honest assessment: pure price arbitrage across major crypto exchanges is no longer a viable retail strategy. The reasons are structural:

1. **Bot saturation:** Thousands of automated arbitrage bots run continuously on every major exchange. Any price gap that opens is met with immediate competing orders. The effective window for manual intervention is zero.
2. **Pre-funded account requirement:** True arbitrage requires capital sitting idle on multiple exchanges simultaneously, ready to deploy. This capital earns nothing while waiting and carries exchange counterparty risk (exchange hacks, insolvencies like FTX).
3. **API rate limits:** Exchanges limit how often you can query prices and submit orders. Bots with co-location agreements and higher API tiers have structural advantages.
4. **MEV in DeFi:** On-chain arbitrage is dominated by sophisticated MEV bots that can detect your transaction in the mempool and execute before you at the block level.

Retail-accessible "arbitrage" tends to be funding rate arbitrage (holding spot long while shorting perpetuals to collect positive funding), which is a legitimate yield strategy but carries its own risks and is not pure arbitrage.

---

## Key Takeaways

- Arbitrage exploits price discrepancies for the same asset across different markets; in crypto, these arise from fragmented exchanges, regional capital flows, and AMM pricing lag.
- Three main types: exchange arbitrage (same asset, different exchanges), triangular arbitrage (three pairs on one exchange), and DeFi arbitrage (CEX vs DEX price gaps via MEV bots).
- Pure arbitrage requires pre-funded accounts on all exchanges involved — transfer time eliminates most opportunities before they can be acted on.
- Fees (taker fees, withdrawal costs, gas, slippage) routinely consume 50–100% of the apparent profit margin on typical price gaps.
- Price gaps between major exchanges for liquid assets typically close within 5–30 seconds, making manual execution impossible.
- Retail arbitrage across major exchanges is effectively dead — the space is dominated by automated bots with speed, capital, and API advantages that retail traders cannot match.
- Legitimate retail yield strategies (funding rate arbitrage, cross-DEX LP strategies) exist but carry distinct risks and should not be confused with risk-free price arbitrage.
