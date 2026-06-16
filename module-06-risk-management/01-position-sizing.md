# Lesson 06.01: Position Sizing — The Most Important Skill in Trading

## Why Position Sizing Determines Your Survival

Most new traders obsess over finding the perfect entry point or the hottest indicator. Experienced traders know the truth: **position sizing is the single most important skill in trading**. You can have a strategy that wins only 40% of the time and still be highly profitable — if you size your positions correctly. Conversely, a strategy with a 70% win rate can blow up an account if position sizes are reckless.

Position sizing answers one fundamental question: **how much of my capital should I risk on this single trade?** Get this wrong, and a string of normal, expected losses can wipe you out before your edge has time to play out.

---

## The 1-2% Rule: Your Financial Firewall

The most widely used professional risk management rule is simple: **never risk more than 1-2% of your total account on any single trade**.

This rule exists for a mathematically powerful reason — survival. If you risk 2% per trade, you would need to lose 50 consecutive trades in a row to lose your entire account. Even a flawed strategy rarely loses 50 times in a row. This gives your strategy time to work.

**Practical example:**

- Account size: $10,000
- Risk per trade: 1% = **$100 maximum loss per trade**

This $100 is the absolute most you should lose if the trade hits your stop loss. Everything flows from this number.

---

## The Position Size Formula

Once you know your maximum dollar risk, you can calculate exactly how many units to buy:

```
Position Size = (Account × Risk%) / (Entry Price - Stop Loss Price)
```

This formula works for any asset. The denominator is your **risk per unit** — how much you lose per coin, share, or contract if your stop is hit.

### Worked Example: Bitcoin Trade

- **BTC price at entry:** $65,000
- **Stop loss level:** $63,000
- **Risk per BTC:** $65,000 - $63,000 = **$2,000**
- **Account size:** $10,000
- **Risk percentage:** 1% = $100

```
Position Size = $100 / $2,000 = 0.05 BTC
```

You should buy **0.05 BTC** (worth $3,250). If BTC drops to $63,000 and your stop triggers, you lose exactly $100 — your predetermined maximum.

Notice: you are not putting your entire $10,000 into BTC. You are only deploying $3,250, which is appropriate given the stop distance.

---

## The Kelly Criterion: Optimal Bet Sizing

The **Kelly Criterion** is a mathematical formula developed by John Kelly at Bell Labs that calculates the theoretically optimal fraction of your capital to risk on each trade.

### The Formula

```
f* = (bp - q) / b
```

Where:
- **f*** = fraction of capital to bet
- **b** = odds (reward-to-risk ratio)
- **p** = probability of winning (win rate)
- **q** = probability of losing = 1 - p

### Kelly Example

Suppose your strategy has:
- **Win rate (p):** 60% (0.60)
- **Reward-to-risk ratio (b):** 1.5:1
- **Loss rate (q):** 40% (0.40)

```
f* = (1.5 × 0.60 - 0.40) / 1.5
f* = (0.90 - 0.40) / 1.5
f* = 0.50 / 1.5
f* = 0.333 → 33.3%
```

Full Kelly says risk 33.3% of your capital. **This is far too aggressive for most traders.** The Kelly formula assumes perfect knowledge of your true win rate and reward ratio — numbers that fluctuate in real markets.

### Half-Kelly: The Professional Choice

Most professional traders use **half-Kelly** or even quarter-Kelly to account for uncertainty:

- Full Kelly: 33.3% → **Half-Kelly: 16.7%**

Even half-Kelly can feel aggressive. For crypto's extreme volatility, staying within the **1-2% rule** is the safer default, especially for newer traders.

---

## Why Over-Leveraging Destroys Accounts: Ruin Probability

**Ruin probability** is the mathematical likelihood that a trading strategy will eventually lose everything. Even profitable strategies can go bankrupt if position sizes are too large.

Consider two traders, both with a 55% win rate and 1:1 reward/risk:

| Trader | Risk per Trade | Ruin Probability |
|--------|---------------|------------------|
| A      | 2%            | Near 0%          |
| B      | 20%           | Very high        |

Trader B's strategy is mathematically profitable, but the large position sizes mean inevitable variance can wipe the account before the edge plays out over enough trades.

**The math of recovery** makes losses even more devastating with large sizes:
- Lose 10% → need 11.1% to recover
- Lose 25% → need 33.3% to recover
- Lose 50% → need **100%** to recover
- Lose 75% → need **300%** to recover

Large drawdowns become nearly impossible to recover from. Small, consistent position sizes keep you in the game.

---

## Scaling In and Out of Positions

Rather than entering a full position at once, **scaling in** means building your position in increments:

- **Initial entry:** 50% of planned position at the first signal
- **Add on confirmation:** 25% more when price confirms direction
- **Final add:** 25% more on continued momentum

Benefits:
- Reduces average entry cost if price moves against you initially
- Allows you to test the trade with less capital at risk
- Psychologically easier to manage

**Scaling out** (taking partial profits) mirrors this on the exit side:
- Take **50% off** at your first profit target (1R)
- Take **25% off** at your second target (2R)
- Let the final **25% run** with a trailing stop

This strategy locks in profits while leaving room for larger moves.

---

## Building the Habit

Position sizing must become automatic, not optional. Before every trade:

1. Check your account size
2. Calculate your maximum dollar risk (1-2%)
3. Identify your stop loss level
4. Apply the position size formula
5. Verify the position fits within your rules

This process takes 60 seconds and can save you from catastrophic losses.

---

> ## Key Takeaways
>
> - **Position sizing, not strategy selection, is the most important factor in long-term trading survival.**
> - The **1-2% rule**: never risk more than 1-2% of your account on a single trade.
> - Use the formula: **Position Size = (Account × Risk%) / (Entry - Stop Loss)** to calculate exact trade sizes.
> - On a $10,000 account with 1% risk and a $2,000 stop distance, buy only **0.05 BTC**.
> - The **Kelly Criterion** provides a mathematical optimal bet size; use **half-Kelly or less** in practice.
> - **Ruin probability** shows that even profitable strategies go bankrupt with oversized positions.
> - Losing 50% requires a 100% gain to recover — large losses are mathematically crippling.
> - **Scale in** (build positions gradually) and **scale out** (take partial profits) to manage risk dynamically.
