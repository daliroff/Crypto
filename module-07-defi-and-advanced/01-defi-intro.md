# Introduction to Decentralized Finance (DeFi)

Decentralized Finance, or DeFi, refers to financial services and products built on public blockchains that operate without centralized intermediaries like banks, brokerages, or exchanges. Instead of trusting a company to hold your funds and execute transactions, you interact directly with self-executing code — smart contracts — deployed on networks like Ethereum. Anyone with an internet connection and a crypto wallet can access these protocols. There are no sign-up forms, no credit checks, and no business hours.

## What Makes Finance "Decentralized"

Traditional finance depends on trusted third parties: you deposit money at a bank and trust that the bank will honor withdrawals, execute trades, and keep accurate records. DeFi replaces that trust with cryptographic guarantees. The rules of a lending pool or an exchange are written into smart contract code that anyone can read and audit. No single company controls the funds; users retain custody through their own wallets. This permissionless design means anyone, anywhere in the world, can participate on equal terms.

The trade-off is that there is no customer support hotline and no regulatory backstop. If you lose your private keys or send funds to the wrong address, recovery is generally impossible. DeFi transfers power — and responsibility — to the individual user.

## Smart Contracts: The Engine of DeFi

A smart contract is a program stored on a blockchain that automatically executes when predefined conditions are met. Think of it as a vending machine: you insert the correct input, and the machine dispenses the output — no cashier required. In DeFi, smart contracts hold funds in escrow, calculate interest rates in real time, issue and burn tokens, and settle trades atomically.

Ethereum pioneered programmable smart contracts and remains the dominant DeFi platform. Other smart-contract chains — Solana, Avalanche, BNB Chain, Arbitrum — have grown their own ecosystems. Each contract is immutable once deployed (unless designed with upgrade mechanisms), which is both a security feature and a limitation.

## Key DeFi Primitives

**Decentralized Exchanges (DEXs):** Platforms like Uniswap and Curve allow users to swap tokens directly from their wallets. Unlike centralized exchanges, there is no order book managed by a company; instead, trades execute against liquidity pools funded by other users.

**Lending and Borrowing:** Protocols like Aave and Compound allow users to deposit assets as collateral and borrow other assets against them, or to earn interest by supplying liquidity to lending pools. Interest rates adjust algorithmically based on supply and demand.

**Stablecoins:** Tokens designed to maintain a stable value, typically pegged to the US dollar. USDC and USDT are centrally issued. DAI, issued by MakerDAO, is decentralized — it is minted by users locking up collateral in smart contracts. Stablecoins are the lifeblood of DeFi because they let participants avoid volatility while staying on-chain.

**Yield Aggregators:** Protocols like Yearn Finance automatically move user deposits across lending and liquidity protocols to maximize returns, removing the manual work of chasing the best rates.

## Total Value Locked (TVL)

TVL — Total Value Locked — is the primary metric used to measure DeFi adoption. It represents the aggregate value of all assets deposited into DeFi smart contracts at a given moment. When TVL for a protocol rises, it signals growing user trust and liquidity. When TVL collapses sharply, it often indicates a loss of confidence, a security exploit, or a market-wide sell-off.

TVL is a useful but imperfect indicator. It is denominated in USD, so a drop in token prices can reduce TVL even when no funds have left the protocol. It also does not account for leveraged or double-counted positions. Use it as a directional signal, not a precise measure of value creation.

## Major Protocols to Know

- **Uniswap:** The largest DEX by volume. Pioneered the Automated Market Maker (AMM) model. Its v3 design introduced concentrated liquidity, allowing LPs to focus capital in specific price ranges.
- **Aave:** A leading decentralized lending protocol. Users deposit assets to earn yield or borrow against collateral. Introduced flash loans — uncollateralized loans that must be repaid within a single transaction block.
- **Compound:** One of the earliest lending protocols. Similar to Aave, it popularized algorithmic interest rates and governance token distribution to users.
- **MakerDAO:** Issues DAI, one of the oldest decentralized stablecoins. Users open "vaults," lock collateral (ETH, wBTC, and others), and mint DAI against it. The system automatically liquidates under-collateralized positions.

## Risks in DeFi

**Smart Contract Bugs:** Code is not infallible. Exploits have drained hundreds of millions of dollars from protocols through logic errors, re-entrancy attacks, and oracle manipulation. Even audited code has been exploited.

**Rug Pulls and Exit Scams:** Malicious developers can build protocols with hidden backdoors that allow them to drain liquidity pools or mint unlimited tokens, then disappear. Projects with anonymous teams and unaudited contracts carry the highest risk.

**Liquidation Risk:** In lending protocols, if the value of your collateral falls below a threshold, the protocol automatically sells it to repay your loan. A sudden price crash can trigger cascading liquidations.

**Oracle Risk:** DeFi protocols rely on price feeds (oracles) to determine asset values. If an oracle is manipulated or fails, protocols can be tricked into mispricing assets.

**Regulatory Risk:** DeFi operates in a legal gray zone in many jurisdictions. Regulatory changes could restrict access or create compliance requirements that alter how protocols function.

---

## Key Takeaways

- DeFi uses smart contracts on public blockchains to recreate financial services without centralized intermediaries.
- The core primitives are DEXs, lending protocols, stablecoins, and yield aggregators.
- Major protocols include Uniswap, Aave, Compound, and MakerDAO.
- TVL (Total Value Locked) measures how much capital is deposited in DeFi protocols — useful as a directional signal, not a precise valuation tool.
- The main risks are smart contract vulnerabilities, rug pulls, liquidation cascades, oracle failures, and regulatory uncertainty.
- DeFi is permissionless: no gatekeepers, but also no safety net. Self-custody means full personal responsibility.
