# Lesson 07.01: Introduction to DeFi — Finance Without Intermediaries

## What Is DeFi?

**DeFi (Decentralized Finance)** refers to financial services and products built on public blockchains — primarily Ethereum — that operate without traditional intermediaries like banks, brokers, or exchanges. In DeFi, the rules are enforced by code, not by institutions, and anyone with an internet connection and a crypto wallet can participate.

Traditional finance (TradFi) requires you to trust an institution at every step:
- Depositing money → trust your bank
- Getting a loan → trust a bank's approval process
- Trading stocks → trust a broker
- Sending money internationally → trust multiple correspondent banks

DeFi replaces these trusted intermediaries with **smart contracts** — programs that run on the blockchain and execute automatically when predefined conditions are met.

---

## Smart Contracts: The Engine of DeFi

A **smart contract** is self-executing code deployed on a blockchain. Once deployed, it runs exactly as programmed — no one can alter it, censor it, or stop it (in most designs). The Ethereum blockchain and its **EVM (Ethereum Virtual Machine)** is the dominant platform for smart contracts, though others like Solana, Avalanche, and BNB Chain also host significant DeFi ecosystems.

### The Vending Machine Analogy

The best way to understand a smart contract is the **vending machine**:

- A vending machine holds products and has a set of rules: "Insert $2.00, press B4, receive a bag of chips."
- No human cashier is needed. The machine enforces the rules automatically.
- As long as you follow the rules (insert money, press the button), you get your item.

A DeFi lending protocol like Aave works the same way:
- "Deposit 1 ETH as collateral → Borrow up to $1,200 USDC at the current borrow rate."
- No loan officer reviews your application. No credit check. The contract checks your collateral and executes.
- If your collateral falls below the required ratio, the contract automatically liquidates your position.

---

## Key DeFi Primitives

DeFi replicates and extends core financial services:

- **Lending and Borrowing:** Deposit assets as collateral and borrow other assets (Aave, Compound)
- **Decentralized Trading:** Exchange tokens directly on-chain without a centralized exchange (Uniswap, Curve)
- **Yield Generation:** Earn interest or rewards by providing capital to protocols
- **Stablecoins:** Algorithmically or collateral-backed stable-value tokens (DAI by MakerDAO)
- **Insurance:** Protocol coverage against smart contract exploits (Nexus Mutual)
- **Derivatives:** On-chain perpetuals, options, and synthetic assets (GMX, dYdX)

---

## Major DeFi Protocols

### Uniswap — The Decentralized Exchange (DEX)

Uniswap allows users to swap any ERC-20 token directly from their wallet using **Automated Market Makers (AMMs)** — liquidity pools of paired tokens instead of traditional order books. It has processed hundreds of billions in trading volume and pioneered the model that nearly every DEX now follows.

### Aave — Decentralized Lending

Aave is a lending protocol where users deposit supported assets (ETH, USDC, WBTC, etc.) to earn interest, or post collateral to borrow against. Interest rates adjust algorithmically based on supply and demand. Aave also pioneered **flash loans** — uncollateralized loans that must be borrowed and repaid within a single transaction block, enabling arbitrage and liquidation strategies impossible in traditional finance.

### Compound — Money Markets

Compound pioneered the concept of **cTokens** — interest-bearing tokens representing your deposit. Deposit USDC, receive cUSDC that continuously appreciates as interest accrues. Compound also popularized **liquidity mining** by distributing its COMP governance token to protocol users.

### MakerDAO — Decentralized Stablecoin

MakerDAO allows users to lock ETH (or other approved collateral) in a **vault** and mint **DAI**, a USD-pegged stablecoin. DAI maintains its peg through overcollateralization and algorithmic stability mechanisms — no central bank or fiat reserves required.

### Curve Finance — Stablecoin DEX

Curve is specialized for swapping between stablecoins and like-priced assets (USDC/USDT, ETH/stETH) with minimal **slippage**. Its low-slippage AMM design makes it the backbone of stablecoin liquidity in DeFi, and the Curve Wars — protocols competing to control its liquidity incentives — became one of DeFi's most interesting game-theoretic events.

---

## TVL: The Key Metric for DeFi

**TVL (Total Value Locked)** measures the total capital deposited into DeFi protocols. It is the primary metric for assessing DeFi's scale and an individual protocol's adoption.

- DeFi TVL peaked at approximately **$180 billion** in November 2021
- TVL is tracked in real time on **DefiLlama.com**, broken down by protocol, blockchain, and category
- A protocol with rising TVL is attracting capital; falling TVL signals withdrawals

**Important caveat:** TVL can overstate true unique capital. The same ETH can be deposited in Aave, borrowed as USDC, deposited in Curve, and counted at each step. TVL is a directional indicator, not a measure of unique capital deployed.

---

## DeFi Risks: What Can Go Wrong

DeFi's openness and composability create unique risks:

### Smart Contract Bugs
Code has bugs. DeFi protocols have lost billions to exploits. The Ronin Bridge hack ($625M, 2022), the Wormhole bridge exploit ($320M, 2022), and the Poly Network hack ($610M, 2021) demonstrate that even large, audited protocols are vulnerable. Multiple audits reduce but do not eliminate this risk.

### Oracle Manipulation
DeFi protocols need real-world price data. They get this from **oracles** — data feeds like Chainlink. Attackers have manipulated oracle prices — typically via flash loans distorting the price on a DEX used as an oracle source — to drain lending protocols.

### Liquidation Risk
If you borrow against collateral and the collateral's value drops, your position can be **automatically liquidated** — your collateral is sold to repay the debt, often at a 5-15% penalty. During sharp market drops, cascading liquidations have contributed to price crashes.

### Rug Pulls
Anonymous developers create protocols, attract deposits with high APY incentives, and then drain the treasury (the "rug pull"). The warning signs: anonymous team, unaudited code, very new protocol, no liquidity lockup, suspiciously high yields.

### Regulatory Risk
DeFi operates in a legal gray area globally. Regulatory enforcement actions against specific protocols, front-ends, or their developers can cause rapid value destruction and force protocol shutdowns.

---

## Gas Fees: The Cost of Ethereum DeFi

Every Ethereum transaction requires paying **gas** — a fee paid to validators for processing your transaction. During high-demand periods, Ethereum gas fees can be:

- Simple token transfer: $2-20
- DEX swap on Uniswap: $20-100+
- Complex multi-step DeFi interactions: $100-500+

This makes Ethereum DeFi **economically impractical for small positions**. Paying $50 in gas to yield-farm a $500 position wipes out months of returns.

**Solutions — Layer 2 Networks:**
- **Arbitrum:** Ethereum-compatible L2 using optimistic rollups, gas typically $0.10-2.00
- **Polygon (MATIC):** EVM-compatible sidechain, gas often under $0.01
- **Base:** Coinbase-backed L2, low fees with growing DeFi ecosystem
- **Optimism:** Optimistic rollup L2, home to major DeFi deployments

Most major DeFi protocols are now deployed on multiple chains and L2s. For most users with smaller positions, L2s are the practical entry point.

---

## DeFi vs CeFi Comparison

| Feature              | DeFi                                 | CeFi (Centralized Exchange)         |
|----------------------|--------------------------------------|-------------------------------------|
| Custody of funds     | You control via wallet (non-custodial) | Exchange holds your funds           |
| KYC / Identity       | None required                        | Required (passport, ID verification)|
| Access               | Anyone with a wallet                 | Geographic restrictions may apply   |
| Transparency         | All transactions visible on-chain    | Opaque internal database            |
| Counterparty risk    | Smart contract exploit risk          | Exchange insolvency (cf. FTX, 2022) |
| Transaction speed    | Blockchain confirmation (seconds)    | Instant (internal ledger)           |
| Fees                 | Gas fees (variable, can be high)     | Trading fees (fixed, typically low) |
| Customer support     | None — code is law                   | Support teams available             |
| Asset selection      | Any token with a liquidity pool      | Curated list of approved assets     |

---

> ## Key Takeaways
>
> - **DeFi** provides financial services — lending, trading, yield generation — through smart contracts on public blockchains, replacing trusted intermediaries with trustless code.
> - **Smart contracts** are like vending machines: deposit the right input, get the specified output automatically, with no human in the loop.
> - The five major DeFi primitives are lending, trading, yield, stablecoins, and insurance.
> - Key protocols to know: **Uniswap** (DEX), **Aave** (lending), **Compound** (money markets), **MakerDAO** (DAI stablecoin), **Curve** (stablecoin swaps).
> - **TVL (Total Value Locked)** is the headline DeFi metric — track it on DefiLlama.com.
> - Critical DeFi risks: smart contract exploits, oracle manipulation, liquidation, rug pulls, regulatory action.
> - **Ethereum gas fees** can be very high — Layer 2 networks (Arbitrum, Polygon, Base) make DeFi economical for smaller positions.
> - DeFi is **non-custodial** (you control your keys); CeFi is custodial (the exchange holds your funds). FTX's collapse in 2022 is the defining lesson in why custodial risk matters.
