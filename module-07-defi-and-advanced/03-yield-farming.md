# Yield Farming

Yield farming is the practice of putting crypto assets to work across DeFi protocols to earn the highest possible return. The term evokes images of planting capital and harvesting profits — and like agriculture, it involves real labor, real risk of crop failure, and seasons of abundance followed by drought. At its peak in 2020 and 2021, yield farming offered returns that dwarfed anything in traditional finance. Understanding how those yields are generated — and why many of them vanish quickly — is essential before committing capital.

## How Yield Farming Works

At its simplest, yield farming stacks multiple sources of income on top of each other:

**1. Liquidity provision fees.** When you deposit assets into an AMM pool, every swap that routes through your pool pays you a fraction of the trading fee. This is the baseline layer of income.

**2. Governance token rewards.** Many DeFi protocols distribute their own native tokens to users who supply liquidity or lend assets. These "liquidity mining" rewards were designed to bootstrap adoption by incentivizing early participation. Protocols like Compound, Uniswap, and Curve have all distributed governance tokens this way. The dollar value of these token emissions can dwarf the underlying fee income — but only if the token holds its value.

**3. Staking and compounding.** Some protocols reward you for staking LP tokens in a "farm" contract on top of your pool position. You can then take those rewards, sell them for more of the base assets, re-deposit, and compound your position. Automated vaults (like those built on Yearn or Beefy Finance) do this compounding on your behalf, often dozens of times per day.

The farmer who moves capital fluidly between these layers — chasing the highest risk-adjusted return — is the archetypal "yield farmer."

## APY vs APR: Understanding the Numbers

**APR (Annual Percentage Rate)** is the simple annualized return without compounding. If a pool pays 1% per month in fees, its APR is 12%.

**APY (Annual Percentage Yield)** accounts for compounding. If you reinvest that 1% monthly, at year-end you have:

```
(1 + 0.01)^12 - 1 = 12.68% APY
```

The more frequently you compound, the higher the APY relative to APR. Daily compounding of a 60% APR yields approximately:

```
(1 + 0.60/365)^365 - 1 ≈ 82% APY
```

DeFi protocols almost always advertise APY, not APR. Automated vaults compound continuously and can show legitimately high APYs. The danger is that many platforms display APY figures calculated from a snapshot of the current token emission rate, which changes daily or even hourly as more capital enters the farm, diluting everyone's share of the rewards.

## The Risks of Yield Farming

**Smart contract risk.** Every additional protocol you interact with adds another potential point of failure. A farm that routes through four contracts — the AMM, the LP staking contract, the reward distributor, and a compounder vault — is exposed to four independent sets of code. A single exploit can drain all deposited funds with no recourse.

**Token inflation and sell pressure.** High APYs denominated in governance tokens are almost always self-defeating. As the protocol mints tokens to pay farmers, early recipients sell for profit, increasing sell pressure. The token price falls, reducing the dollar value of future rewards. This cycle — high APY attracts capital, emissions dilute token price, APY falls in dollar terms, capital rotates out — is so predictable it has a name: "mercenary capital." Many farming tokens have declined 90%+ from their launch prices.

**Impermanent loss.** As covered in the liquidity pools module, IL can erode principal faster than fee income replenishes it, particularly in volatile asset pairs.

**Liquidation risk.** Some advanced farming strategies borrow assets to lever up positions. If collateral values drop, these positions can be liquidated, wiping out the equity.

**Rug pulls and exit scams.** Anonymous teams can deploy "farm" contracts with hidden admin keys that allow them to drain deposited funds. Projects that copy-paste code, launch without an audit, and promise 1,000%+ APYs are extremely high-risk.

## Realistic vs. Advertised Yields

A farm advertising 500% APY will almost never deliver 500% for more than a few days or weeks. Advertised yield reflects the emission rate at a single point in time; it collapses as:

- More capital enters, reducing each farmer's share of fixed emissions.
- The reward token depreciates under sell pressure.
- Emission schedules step down by design.

Sustainable, realistic yield from established protocols tends to look more like:
- Stablecoin lending on Aave or Compound: 3–8% APY depending on market conditions.
- Blue-chip AMM pools (ETH/USDC, WBTC/ETH) on Uniswap v3: 5–20% APY in active ranges.
- Stablecoin AMM pools (Curve 3pool): 2–6% APY.

Anything above 20% APY in a stablecoin pool or above 50% in a volatile pair warrants serious scrutiny.

## Safe vs. Risky Farms: A Checklist

**Lower risk indicators:**
- Protocol has been live for 12+ months without a major exploit.
- Code is audited by a reputable firm (Trail of Bits, OpenZeppelin, Certik with caveats).
- Rewards denominated in established assets or blue-chip tokens.
- Team is doxxed (publicly identified) or protocol is fully decentralized.
- Large TVL signals that many sophisticated users have assessed and accepted the risk.
- Rewards can be claimed and sold independently without lock-up.

**Higher risk indicators:**
- Launched less than 30 days ago.
- Unaudited or self-audited contracts.
- APY above 500%.
- Anonymous team with no track record.
- TVL under $1M (thin liquidity, easy to drain).
- Reward token has no utility beyond farming.
- Requires locking funds for 6+ months with no exit option.

---

## Key Takeaways

- Yield farming stacks fee income, governance token rewards, and compounding to maximize returns on deposited assets.
- APY accounts for compounding and is almost always higher than APR; understand which figure a platform is displaying.
- Advertised APYs collapse quickly as more capital enters a farm and as reward token prices fall — sustainable yields on reputable protocols are typically 3–20%.
- Core risks are smart contract exploits, token inflation eroding reward value, impermanent loss, and outright rug pulls.
- Before entering a farm, assess: audit status, protocol age, team transparency, TVL, and whether the yield source is sustainable.
- The safest yield farming starts with established protocols, blue-chip assets, and yield sources grounded in real fee income rather than speculative token emissions.
