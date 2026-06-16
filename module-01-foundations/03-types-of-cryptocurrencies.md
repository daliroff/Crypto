# Lesson 3: Types of Cryptocurrencies

## Introduction

Walk into any crypto conversation and you'll hear terms thrown around — altcoins, stablecoins, governance tokens, meme coins, wrapped tokens. The crypto market has thousands of assets, and not all of them are trying to do the same thing. Understanding how to categorize them is one of the most practical skills you can develop as a trader or investor.

This lesson breaks down every major category, with real examples, and explains what questions to ask before putting money into any of them.

---

## Layer 1 Coins: The Base Blockchains

**Layer 1 (L1)** refers to a base blockchain that processes and finalizes transactions on its own chain. These are the foundation — everything else is built on top of them.

### Bitcoin (BTC)
- **Purpose**: Decentralized, censorship-resistant store of value and peer-to-peer payment system
- **Key stats**: 21 million hard cap, ~10-minute block times, PoW consensus
- **Strengths**: Most secure, most decentralized, longest track record, highest liquidity
- **Weaknesses**: Limited programmability, slow transaction finality, high energy use
- **Use case as a trader**: The market benchmark. When BTC goes down, almost everything goes down with it. BTC dominance (BTC's share of total market cap) is a key indicator of market sentiment.

### Ethereum (ETH)
- **Purpose**: Programmable blockchain — the backbone of DeFi, NFTs, and Web3
- **Key stats**: No hard supply cap (but deflationary via EIP-1559 fee burning), ~12-second block times, PoS consensus since September 2022
- **Strengths**: Largest developer ecosystem, most DeFi TVL (Total Value Locked), EVM compatibility adopted by many competitors
- **Weaknesses**: High gas fees during congestion, slower than newer L1s
- **Use case as a trader**: ETH is the "**reserve currency of DeFi**." High network activity drives up demand for ETH as gas.

### Solana (SOL)
- **Purpose**: High-performance blockchain optimized for speed and low cost
- **Key stats**: Theoretical 65,000 TPS (though real-world sustained throughput is lower), sub-second finality, ~$0.00025 per transaction
- **Consensus**: Proof of History (PoH) combined with Proof of Stake — a unique timestamp mechanism that helps validators agree on the order of events
- **Strengths**: Extremely fast, cheap, thriving NFT and DeFi ecosystem, strong developer adoption
- **Weaknesses**: History of network outages (2021-2022), more centralized validator set than Ethereum
- **Use case as a trader**: Solana is highly volatile and tends to amplify bull market moves. SOL's price correlates with activity on the Solana DeFi/NFT ecosystem.

### Avalanche (AVAX)
- **Purpose**: A network of interoperable blockchains with fast finality
- **Architecture**: Three built-in chains — the **X-Chain** (asset transfers), **C-Chain** (EVM-compatible smart contracts), and **P-Chain** (validators/subnets)
- **Consensus**: Novel Avalanche consensus — probabilistic, sub-second finality, highly scalable
- **Strengths**: EVM-compatible (easy for Ethereum developers to port projects), subnet architecture allows custom blockchains for enterprises
- **Weaknesses**: Smaller ecosystem than Ethereum or Solana, high initial validator requirements

### How to Compare L1s
When evaluating an L1, ask:
- What is its **security model** (PoW, PoS, other)?
- How **decentralized** is the validator set?
- What is the **developer ecosystem** like (GitHub activity, TVL, dApp count)?
- What is the **fee and throughput** story?
- Does it have **real usage**, or just speculation?

---

## Altcoins: Everything That Isn't Bitcoin

**Altcoin** (alternative coin) originally meant any cryptocurrency that wasn't Bitcoin. Today it's used loosely to mean any crypto asset outside the top 1-2 by market cap.

- **Risk/reward profile**: Altcoins offer higher potential upside than BTC in bull markets and higher potential downside in bear markets. A 2x move in BTC might be a 10x move (or -90%) in a small-cap altcoin.
- **Liquidity risk**: Smaller altcoins have thin order books — large orders can move the price dramatically
- **Vetting**: Always check team, tokenomics (supply schedule, vesting, inflation), real usage, and competitive moat
- **Market cycle behavior**: Most altcoins follow BTC's lead. The concept of "**altcoin season**" describes periods when capital rotates from BTC into altcoins after BTC has established a trend

---

## Stablecoins: Crypto's Dollar Equivalent

A **stablecoin** is a crypto asset designed to maintain a stable value, typically pegged to the US dollar (1 stablecoin = $1). They exist to give traders and DeFi users the benefits of crypto (fast, permissionless transfers) without the volatility.

### Fiat-Backed Stablecoins
- **USDT (Tether)**: The most widely used stablecoin by volume. Each USDT is supposedly backed by $1 in reserves (cash, treasuries, etc.) held by Tether Ltd.
- **USDC (USD Coin)**: Issued by Circle, backed by fully audited cash and short-term US treasuries. Considered more transparent than USDT.
- **How they maintain peg**: Arbitrage. If USDT trades at $0.99, traders buy cheap USDT and redeem it for $1.00 from Tether. If it trades at $1.01, they mint new USDT and sell it. This arbitrage keeps the price near $1.
- **Risk**: Centralized — the issuer can freeze your wallet (and has). Counterparty risk if reserves are mismanaged.

### Crypto-Backed Stablecoins
- **DAI**: Issued by MakerDAO on Ethereum. You lock up ETH (or other crypto) as collateral — typically 150%+ of the DAI you want to mint. The overcollateralization absorbs price swings in the collateral.
- **Risk**: If collateral value drops too fast (flash crash), positions can be liquidated. DAI has maintained its peg through multiple market crashes.

### Algorithmic Stablecoins
- These attempt to maintain a peg through supply/demand mechanics using code, without direct collateral backing.
- **UST (TerraUSD)**: The most infamous example. UST was paired with LUNA — burning LUNA minted UST and vice versa. In May 2022, a large UST sell-off triggered a **death spiral**: UST depegged → panic → more selling → more depegging → LUNA hyperinflated to worthlessness. Over **$40 billion** in market cap was wiped out in days.
- **Lesson**: Algorithmic stablecoins without hard collateral backing are extremely high risk. Many have failed.

---

## Utility Tokens: Fuel for Ecosystems

**Utility tokens** have a specific function within a protocol or platform. They are not simply currencies — they have embedded utility.

### Gas Tokens
- **ETH**: Required to pay for computation on Ethereum. Every transaction, contract interaction, and DeFi trade burns ETH as gas.
- **SOL**: Required to pay transaction fees on Solana.
- Demand for gas tokens is directly tied to network usage — more activity means more demand.

### Governance Tokens
- **UNI (Uniswap)**: Holders can vote on changes to the Uniswap decentralized exchange — fee structures, liquidity incentives, treasury spending
- **AAVE**: Governance token for the AAVE lending protocol. Also used for staking in the safety module to backstop protocol insolvency risk
- **Risks**: Many governance tokens have minimal "value accrual" — they give voting rights but don't entitle holders to protocol revenue. Always check whether the token has real economic utility or is purely speculative governance rights.

---

## Security Tokens and Regulatory Implications

A **security token** represents ownership in a real-world asset — equity in a company, a share of real estate, a bond. They are regulated financial instruments, subject to the same laws as traditional securities.

- Must comply with **KYC/AML** requirements
- Subject to **SEC oversight** in the United States (and equivalent bodies globally)
- Trading is restricted to accredited investors on compliant platforms
- Examples: tokenized private equity, tokenized real estate through platforms like RealT
- **Why it matters for traders**: The SEC's ongoing battle over which crypto tokens constitute "unregistered securities" (the Ripple/XRP case, the Coinbase lawsuit) has major implications for the entire market. Tokens ruled to be securities face delistings and legal risk.

---

## Meme Coins: Speculation vs. Fundamentals

**Meme coins** are cryptocurrencies with no inherent utility — they derive value almost entirely from community enthusiasm, cultural relevance, and speculative momentum.

- **DOGE (Dogecoin)**: Created in 2013 as a joke based on the Shiba Inu meme. Became worth over **$80 billion** at its peak in 2021, largely driven by Elon Musk tweets. Has an unlimited supply with ~5 billion new DOGE mined per year.
- **SHIB (Shiba Inu)**: A "DOGE killer" with a quadrillion token supply. Rode the 2021 meme coin wave to a multi-billion dollar market cap.

### The Hard Truth About Meme Coins
- Some traders have made extraordinary returns on meme coins — but survivorship bias is severe. For every 100x winner, there are thousands of coins that went to zero.
- Meme coins are driven by **narrative momentum**, not fundamentals. Timing the entry and exit is extremely difficult.
- **Pump and dump risk**: Low-cap meme coins are prime targets for coordinated manipulation.
- If you trade meme coins, treat it as speculation, not investment. Size positions accordingly.

---

## Wrapped Tokens: Bringing Assets Cross-Chain

A **wrapped token** is a tokenized version of a cryptocurrency that exists on a different blockchain.

### WBTC (Wrapped Bitcoin)
- Bitcoin is native to the Bitcoin blockchain and cannot be used in Ethereum smart contracts natively
- **WBTC** is an ERC-20 token on Ethereum, backed 1:1 by real Bitcoin held in custody by BitGo (a custodian)
- Allows Bitcoin holders to participate in Ethereum DeFi — using BTC as collateral for loans, providing liquidity in AMMs, etc.
- **Process**: Deposit BTC with a custodian → receive WBTC on Ethereum → use in DeFi → burn WBTC to redeem BTC
- **Risk**: Centralization — you're trusting the custodian to hold the Bitcoin. Also smart contract risk on the Ethereum side.

Other examples: **WETH** (Wrapped ETH, needed for some ERC-20 interactions), **stETH** (Lido's staked ETH, representing staked ETH plus accruing rewards).

---

## How to Categorize and Research Any Token

When you encounter an unfamiliar token, work through this checklist:

1. **Category**: Is it a L1, L2, DeFi protocol token, stablecoin, governance token, meme coin?
2. **Whitepaper/documentation**: Does it have a credible technical specification?
3. **Team**: Are the founders public and verifiable? Do they have relevant experience?
4. **Tokenomics**: What is the total supply? Circulating supply? Vesting schedule for team/investors? Inflation rate?
5. **Usage**: Is there real on-chain activity (transactions, TVL, active addresses)?
6. **Competition**: What problem does it solve, and how does it compare to competitors?
7. **Audit history**: Has the code been audited by a reputable firm (Trail of Bits, OpenZeppelin, Certik)?
8. **Community**: Active developer community on GitHub? Engaged community on Discord/forums?
9. **Exchange listings**: Is it on reputable exchanges or only obscure DEXs? (The latter is a risk flag.)

---

## Key Takeaways

> **What to remember from this lesson:**
>
> - **Layer 1 blockchains** (BTC, ETH, SOL, AVAX) are the foundation of crypto. Each has different trade-offs in speed, security, decentralization, and developer ecosystem.
> - **Altcoins** offer higher risk/reward than Bitcoin — they amplify market moves in both directions.
> - **Stablecoins** (USDT, USDC, DAI) are essential tools for traders, but carry their own risks: centralization risk (fiat-backed), smart contract risk (crypto-backed), and death spiral risk (algorithmic).
> - **Utility tokens** derive value from actual use in a protocol — gas tokens (ETH, SOL) are tied directly to network demand.
> - **Governance tokens** (UNI, AAVE) give voting rights but may have limited economic value accrual — check the tokenomics carefully.
> - **Meme coins** (DOGE, SHIB) are pure speculation driven by narrative. Some produce massive gains; most go to zero.
> - **Wrapped tokens** (WBTC) let assets from one blockchain be used on another, at the cost of centralization or smart contract risk.
> - Before investing in any token, research: category, team, tokenomics, real usage, audits, and competition.
