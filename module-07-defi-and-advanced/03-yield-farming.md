# Lesson 07.03: Yield Farming — Putting Your Crypto to Work

## What Is Yield Farming?

**Yield farming** (also called liquidity mining) is the practice of deploying crypto assets across DeFi protocols to earn rewards — interest, trading fees, and/or governance tokens — maximizing the return on your capital.

The term "farming" is apt: you plant your capital in a protocol and harvest rewards over time. Like agriculture, the yields vary dramatically by season, the soil (protocol quality) matters enormously, and some crops fail entirely.

At its peak in the **DeFi Summer of 2020** and through 2021, yield farming offered APYs in the hundreds or thousands of percent. Those eye-watering numbers attracted billions of dollars of capital — and also significant fraud, exploitation, and collapse. Today, the market is more mature: yields are lower, but many protocols generate genuine, sustainable returns.

---

## How Yield Farming Works: The Full Loop

A typical yield farming sequence:

1. **Deposit assets** into a DeFi protocol (e.g., deposit ETH + USDC into Uniswap)
2. **Receive LP tokens** representing your share of the liquidity pool
3. **Stake LP tokens** in the protocol's farm or staking contract
4. **Earn reward tokens** — typically the protocol's governance token (e.g., UNI, SUSHI, CRV)
5. **Claim and reinvest** (compound) rewards, or sell them for stablecoins

The yield has two components:
- **Trading fees** from the underlying liquidity pool (sustainable)
- **Token emissions** — the protocol minting and distributing new governance tokens to incentivize liquidity (inflationary, often not sustainable)

The distinction between these two yield sources is critical to understanding whether a yield is real or illusory.

---

## APY vs. APR: Know the Difference

- **APR (Annual Percentage Rate):** Simple interest, without compounding. If a farm pays 50% APR, you earn 50% of your principal over one year, assuming no reinvestment.
- **APY (Annual Percentage Yield):** Includes the effect of compounding. If you reinvest your rewards daily, a 50% APR becomes approximately 64.8% APY.

The formula to convert APR to APY:
```
APY = (1 + APR/n)^n - 1
```
Where n = number of compounding periods per year.

**Farming dashboards typically display APY** because it looks higher. Always check whether the displayed number assumes manual or automatic compounding, and over what time period it was calculated. APYs in DeFi can change dramatically within hours as new farmers enter or exit.

---

## Real Yield vs. Token Emissions

This is one of the most important distinctions in DeFi yield farming:

### Token Emission Yield (Often Unsustainable)

The protocol mints new governance tokens and distributes them to LPs as rewards. This creates buy-side demand for the token (LPs receiving it may sell) but also increases supply. If more people are selling the reward token than buying it, its price falls — and with it, your APY in dollar terms.

**The Ponzi dynamic:** High emission APYs attract capital → more capital dilutes each LP's reward share → APY falls → capital leaves → token price falls → APY collapses. Many farms of 2020-2021 followed exactly this trajectory.

### Real Yield (Sustainable)

Real yield comes from actual protocol revenue — trading fees, borrowing interest, liquidation fees — distributed to stakers/LPs. This is sustainable because it's backed by genuine economic activity.

**Examples of real yield sources:**
- Uniswap V3 trading fees (0.05%, 0.3%, or 1% per swap depending on pool tier)
- Aave's lending spread (borrowers pay more than depositors earn; the difference is protocol revenue)
- GMX's perpetual trading fees distributed to GLP holders

When evaluating a yield farm, ask: "If the reward token's price went to zero, would there still be any yield?" If no, the yield is purely emission-based.

---

## Popular Yield Farming Strategies

### 1. Stablecoin Pairs — Conservative

- **Assets:** USDC/USDT, DAI/USDC, FRAX/USDC
- **Protocol:** Curve Finance, Uniswap V3, Aave
- **Typical APY:** 3-15%
- **Risks:** Near-zero impermanent loss, smart contract risk, stablecoin depeg risk
- **Best for:** Capital preservation with modest yield

### 2. Blue-Chip Volatile Pairs — Moderate

- **Assets:** ETH/USDC, BTC/ETH, SOL/USDC
- **Protocol:** Uniswap V3, Orca (Solana), Trader Joe (Avalanche)
- **Typical APY:** 10-40% in fee-rich pools
- **Risks:** Significant impermanent loss if prices diverge sharply
- **Best for:** Traders who would hold the assets anyway and want fees on top

### 3. Correlated Asset Pairs — Efficient

- **Assets:** ETH/stETH, BTC/WBTC, USDC/DAI
- **Protocol:** Curve, Balancer
- **Typical APY:** 5-20% with minimal IL
- **Risks:** Depegging risk (stETH temporarily depegged in 2022), smart contract risk
- **Best for:** Maximizing yield while minimizing IL

### 4. New Protocol Incentive Farms — Aggressive

- **Assets:** New protocol's native token paired with ETH or USDC
- **Typical APY:** 100-1,000%+ (emission-based)
- **Risks:** Rug pull, token price collapse, IL, smart contract exploit
- **Best for:** High-risk/high-reward traders who can exit quickly

---

## Risks of Yield Farming

### 1. Smart Contract Risk

Every DeFi protocol is only as safe as its code. Even audited contracts have been exploited. When you deposit funds into a farm, you trust that smart contract completely. Diversify across multiple protocols and never put more than you can afford to lose into a single farm.

### 2. Impermanent Loss

As covered in the previous lesson, providing liquidity to volatile pairs means your position rebalances as prices move. A 5x return on a token you're farming can be largely offset by the IL you suffered as the pool rebalanced.

### 3. Token Price Collapse

Your reward tokens may be worthless by the time you claim them. If a protocol distributes its governance token as yield and that token falls 90%, your high APY meant nothing. This has happened to hundreds of yield farming projects.

### 4. Liquidity Risk (Can't Exit)

Some pools have very low TVL. When you want to withdraw, there may be high slippage or, in extreme cases, insufficient liquidity to exit your position at a reasonable price. Always check pool depth before entering.

### 5. Rug Pull

The most malicious risk: developers drain the protocol's treasury. Signs of a potential rug:
- Anonymous, unverified team
- No audit or very recent audit from an unknown firm
- Extremely high APY with no clear yield source
- Admin keys that can upgrade/drain contracts without timelock
- Large developer token allocation that vests quickly

---

## How to Evaluate a Yield Farm

Before committing capital, run through this checklist:

- **Audit status:** Has the code been audited by a reputable firm (Trail of Bits, Certik, OpenZeppelin)? Was the audit recent and complete?
- **Team credibility:** Is the team doxxed (publicly identifiable)? Do they have a track record?
- **TVL trend:** Is TVL growing steadily or did it spike and start falling? Falling TVL often precedes protocol death.
- **Yield source:** Is the APY from trading fees (real yield) or token emissions? If emissions, what's the token's emission schedule and circulating supply impact?
- **Token distribution:** Are a large percentage of tokens reserved for insiders with short vest schedules? That's a sell pressure time bomb.
- **Timelock on admin functions:** Can developers upgrade or drain contracts immediately, or is there a 24-48 hour timelock that gives users time to exit?
- **Age of protocol:** Older protocols have survived longer and are more battle-tested. Brand-new protocols carry higher risk.

---

## Auto-Compounders: Maximizing Returns Passively

**Auto-compounders** automatically reinvest (compound) your yield farming rewards at regular intervals, converting your reward tokens back into the farming position without manual intervention.

The power of compounding: a 50% APR compounded daily becomes approximately 64.8% APY. Auto-compounders capture this.

**Popular auto-compounders:**
- **Beefy Finance:** Multi-chain auto-compounder, works across Arbitrum, BNB Chain, Polygon, Avalanche, and more
- **Yearn Finance:** Pioneer of automated yield strategies on Ethereum, uses complex "vault" strategies
- **Autofarm:** Cross-chain optimizer

**Trade-offs of auto-compounders:**
- Additional smart contract layer (more risk)
- Auto-compounders charge performance fees (typically 3-10% of yield)
- Compounding creates taxable events in many jurisdictions

---

> ## Key Takeaways
>
> - **Yield farming** means deploying capital in DeFi protocols to earn trading fees, interest, and governance token rewards.
> - The typical loop: **deposit assets → receive LP tokens → stake LP tokens → earn reward tokens → compound or sell rewards**.
> - **APY includes compounding**; APR does not. A 50% APR compounded daily ≈ 64.8% APY.
> - **Real yield** (from trading fees, borrowing interest) is sustainable; **token emission yield** is inflationary and often collapses as the reward token's price falls.
> - Conservative strategy: stablecoin pairs (near-zero IL, 3-15% APY). Aggressive strategy: new protocol farms (100%+ APY, high rug pull and token collapse risk).
> - The five core risks: smart contract exploit, impermanent loss, reward token price collapse, liquidity risk, and rug pulls.
> - Evaluate farms by: audit status, team credibility, TVL trend, yield source sustainability, token distribution, and whether admin functions have a timelock.
> - **Auto-compounders** (Beefy Finance, Yearn) reinvest rewards automatically, capturing compounding returns — at the cost of additional smart contract risk and a performance fee.
