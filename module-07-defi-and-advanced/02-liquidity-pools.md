# Liquidity Pools and Automated Market Makers (AMMs)

Before decentralized exchanges existed, trading on-chain was either impossible or relied on clunky order-book systems that struggled with low liquidity and slow block times. The introduction of liquidity pools and Automated Market Makers (AMMs) solved this problem elegantly. Instead of matching buyers with sellers, AMMs allow trades to execute instantly against a pool of tokens governed by a mathematical formula. This mechanism is the backbone of decentralized trading and one of the most important innovations in DeFi.

## How Traditional Order Books Work

A traditional exchange — whether it is the NYSE or Binance — uses an order book. Buyers post bids (the price they are willing to pay) and sellers post asks (the price they are willing to accept). A trade executes when a bid and ask match. Market makers, typically professional trading firms, continuously post orders on both sides to keep spreads tight and ensure liquidity.

This system works well for centralized, high-throughput environments. On a blockchain, however, placing and canceling orders costs gas fees, and block confirmation times introduce latency. Order-book DEXs have existed (dYdX, Serum) but require specialized infrastructure. AMMs offered a simpler, more elegant solution that any smart contract could implement.

## The Constant Product Formula: x * y = k

The core formula behind the most common AMM design — pioneered by Uniswap v1 and v2 — is deceptively simple:

```
x * y = k
```

Here, `x` is the quantity of token A in the pool, `y` is the quantity of token B, and `k` is a constant. When a user swaps token A for token B, the pool receives more of A and gives out some B — but the product of the two reserves must remain equal to `k`.

**Worked example:**

Suppose a pool holds 100 ETH and 200,000 USDC. The constant is:

```
k = 100 * 200,000 = 20,000,000
```

The implied price is 200,000 / 100 = **$2,000 per ETH**.

Now a trader wants to buy 5 ETH. After the trade, the pool will have 95 ETH. To find how much USDC they must provide:

```
95 * y = 20,000,000
y = 210,526 USDC
```

The pool now holds 210,526 USDC, meaning the trader paid 10,526 USDC for 5 ETH — an effective price of **$2,105 per ETH**. The price moved because the trade shifted the ratio of the two assets. Larger trades cause more slippage. This self-correcting pricing mechanism automatically adjusts to reflect supply and demand without any human intervention.

## Providing Liquidity and LP Tokens

Anyone can become a liquidity provider (LP) by depositing an equal value of both tokens into a pool. If the pool is 50% ETH and 50% USDC by value, you must deposit both in that proportion. In return, the protocol issues you LP tokens representing your share of the pool.

LP tokens are not just receipts — they are composable assets. You can deposit them into other protocols to earn additional yield, use them as collateral, or transfer them to another wallet. When you want to withdraw, you return your LP tokens and receive back your proportional share of both assets plus any accumulated fees.

## Impermanent Loss: The Hidden Cost of Providing Liquidity

Impermanent loss (IL) occurs when the price ratio of the two assets in a pool changes after you deposit. Your position is worth less than if you had simply held the tokens in your wallet.

**ETH/USDC example:**

You deposit into an ETH/USDC pool when ETH is $2,000. You put in 1 ETH + 2,000 USDC (total $4,000). ETH doubles to $4,000.

Because of how the AMM rebalances, your 1 ETH has been partially sold on the way up. At $4,000 ETH your pool position consists of approximately 0.707 ETH + 2,828 USDC = **$5,656 total**.

If you had simply held 1 ETH + 2,000 USDC, you would have $4,000 + $4,000 = **$8,000 total** — wait, let us recalculate from a $4,000 total starting position.

Start: 0.5 ETH + 1,000 USDC = $2,000 total (simpler numbers).
- Hold scenario at $4,000 ETH: 0.5 ETH ($2,000) + 1,000 USDC = **$3,000**
- Pool scenario at $4,000 ETH: ~0.354 ETH + ~1,414 USDC = **$2,828**
- Impermanent loss: ($3,000 - $2,828) / $3,000 = **~5.7%**

When ETH doubles, IL is approximately 5.7%. When ETH 4x, IL reaches ~20%. The loss is "impermanent" because if prices return to their original ratio, IL disappears. It becomes permanent only when you withdraw at an unfavorable ratio.

## When Is IL Worthwhile?

IL is a cost, but fee income can offset it. A pool with high trading volume generates significant fees — Uniswap charges 0.05%, 0.3%, or 1% per swap depending on the pool tier, distributed proportionally to LPs. If your fee earnings exceed your IL, you come out ahead.

IL is generally more tolerable when:
- The two assets are highly correlated (e.g., USDC/USDT or ETH/stETH), because the price ratio rarely changes.
- Trading volume in the pool is very high, generating substantial fees.
- You are comfortable holding both assets regardless.

IL is most damaging when:
- One asset makes a large directional move (a volatile token vs. a stablecoin).
- Trading volume is thin, so fee income is insufficient to compensate.
- You withdraw during a period of peak price divergence.

---

## Key Takeaways

- AMMs replace order books with liquidity pools and mathematical formulas that automatically price trades.
- The constant product formula (x * y = k) is the foundation of Uniswap-style DEXs: the pool always rebalances so the product of the two reserves stays constant.
- LPs deposit equal value of both assets, receive LP tokens as receipts, and earn a share of trading fees.
- Impermanent loss occurs when the price ratio of pooled assets changes — a 2x move in one asset causes roughly 5.7% IL; a 4x move causes roughly 20%.
- IL is offset by fee income; correlated-asset pools and high-volume pools make LP positions more profitable.
- LP tokens are composable: they can be used across other DeFi protocols to stack additional yield.
