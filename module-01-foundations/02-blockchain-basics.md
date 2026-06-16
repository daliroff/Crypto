# Lesson 2: Blockchain Basics

## Introduction

Blockchain is the foundational technology underneath every major cryptocurrency. Understanding how it works — really works, not just the buzzword version — will make you a significantly better trader and investor. When you know *why* Bitcoin transactions are irreversible, *why* confirmations matter, and *why* 51% attacks are theoretically possible, you make better decisions with your money.

A **blockchain** is a continuously growing list of records (called **blocks**) that are linked together and secured using cryptography. Once data is written to the blockchain, it is practically impossible to alter without redoing an enormous amount of work.

---

## What a Blockchain Actually Is

Imagine a Google Doc that thousands of people have open simultaneously — but unlike a Google Doc, **no single person can edit past entries**. Every new addition must be agreed upon by the majority of participants before it becomes permanent.

More precisely, a blockchain is a **distributed ledger**: a database that is shared and synchronized across a network of computers (nodes). There is no master copy. Every node holds a full copy of the entire transaction history.

This solves a fundamental problem: **how do you get strangers who don't trust each other to agree on a shared record of truth?**

---

## Hash Functions: The Cryptographic Glue

Before understanding blocks, you need to understand **hash functions**. A hash function takes any input and produces a fixed-length output called a **hash** (or digest). The key properties:

- **Deterministic**: the same input always produces the same output
- **One-way**: you cannot reverse-engineer the input from the output
- **Avalanche effect**: changing even one character in the input completely changes the output
- **Fixed length**: regardless of input size, output is always the same length

Bitcoin uses **SHA-256** (Secure Hash Algorithm 256-bit). Here's an example:

- Input: `"Hello"` → SHA-256 → `185f8db32921bd46d35cc5f0d73f3...`
- Input: `"hello"` → SHA-256 → `2cf24dba5fb0a30e26e83b2ac5b9e...`

One lowercase letter changes everything. This makes hash functions ideal for detecting tampering: if anyone changes even a single transaction in a block, the block's hash changes completely, breaking the chain.

---

## Block Anatomy

Each block in the blockchain contains several key components:

### Block Header
- **Previous block hash**: the hash of the block immediately before it — this is what creates the "chain"
- **Merkle root**: a single hash that represents all transactions in the block
- **Timestamp**: when the block was created
- **Nonce**: a number miners change when searching for a valid block (more on this below)
- **Difficulty target**: the threshold the block hash must fall below

### Block Body
- **Transaction list**: all the transactions included in this block
- On the Bitcoin network, a single block can contain **thousands of transactions**

### The Merkle Root
All transactions in a block are hashed together in a tree structure called a **Merkle tree**. Each pair of transaction hashes is hashed together, moving up the tree until a single hash remains — the **Merkle root**. This allows anyone to verify that a specific transaction is in a block without downloading the entire block.

---

## How Nodes Work

A **node** is any computer participating in the blockchain network. There are two main types:

### Full Nodes
- Download and validate the **entire blockchain history** from the Genesis Block to today
- Independently verify every transaction and block against the protocol rules
- Do not trust anyone — they verify everything themselves
- Bitcoin's blockchain is over **500 GB** in size; running a full node requires significant storage
- Full nodes are the backbone of the network's security and decentralization

### Light Nodes (SPV Nodes)
- Download only block **headers**, not full transaction data
- Rely on full nodes to verify transactions
- Much lighter on storage and bandwidth
- Used by mobile wallets like Trust Wallet
- Trade security for convenience — they trust that full nodes are honest

---

## Consensus Mechanisms: How the Network Agrees

With thousands of nodes worldwide, how does the network agree on which transactions are valid and which block gets added next? This is solved by a **consensus mechanism**.

### Proof of Work (PoW)
Used by **Bitcoin** and originally by **Ethereum** (before its merge in 2022).

- Miners compete to solve a computationally expensive puzzle
- The puzzle: find a **nonce** (number used once) such that when combined with the block data and hashed, the result starts with a required number of leading zeros
- This is called finding a hash **below the difficulty target**
- The first miner to find a valid solution **broadcasts the block** to the network
- Other nodes verify the solution instantly (solving is hard; verifying is easy) and add the block to their chain
- The winning miner receives the **block reward** (currently 3.125 BTC after the 2024 halving) plus all transaction fees

**Why "work"?** Because the only way to find the nonce is brute-force guessing — trillions of attempts per second. This work represents real-world energy expenditure, which is what makes attacking the network economically irrational.

### Proof of Stake (PoS)
Used by **Ethereum** (post-Merge), **Solana**, **Avalanche**, **Cardano**, and many others.

- Instead of competing with computing power, validators **stake** (lock up) cryptocurrency as collateral
- Validators are selected to propose new blocks, weighted by their stake
- If a validator tries to cheat (propose invalid transactions), they get **slashed** — losing a portion of their staked funds
- Far more energy-efficient than PoW — Ethereum's energy use dropped by ~99.95% after its Merge to PoS in September 2022
- Critics argue PoS is "**plutocratic**" — those with more coins have more power. PoW advocates argue PoW's energy cost is what gives Bitcoin its unforgeable security

---

## Mining Explained

**Mining** is the process of creating new blocks in a Proof of Work blockchain.

### The Computational Puzzle
Miners are essentially rolling a very large die, over and over, hoping to roll a number below a certain threshold. The "die" is SHA-256, and the "number" they're rolling is the hash of the block header (with different nonces tried each attempt).

### Block Reward and Halving
When a miner successfully mines a block, they earn a **block reward**. For Bitcoin:
- 2009: **50 BTC** per block
- 2012 (1st halving): **25 BTC**
- 2016 (2nd halving): **12.5 BTC**
- 2020 (3rd halving): **6.25 BTC**
- 2024 (4th halving): **3.125 BTC**

Every 210,000 blocks (~4 years), the reward halves. This continues until approximately **2140**, when all 21 million Bitcoin will have been mined. After that, miners will be compensated only by transaction fees.

### Difficulty Adjustment
Bitcoin's protocol automatically adjusts the **mining difficulty** every 2,016 blocks (~2 weeks) to ensure blocks are produced at an average rate of **one every 10 minutes**, regardless of how much mining hardware joins or leaves the network. If more miners join, difficulty goes up. If miners leave, difficulty drops.

---

## Immutability: Why You Can't Edit the Blockchain

This is one of blockchain's most powerful properties. Here's why tampering is practically impossible:

1. Every block contains the **hash of the previous block**
2. If you change any transaction in Block #500, its hash changes
3. That means Block #501's "previous hash" reference is now wrong — it no longer matches
4. You'd have to recompute Block #501 as well, changing its hash
5. This cascades through every subsequent block — you'd have to remine the entire chain from #500 to the present
6. Meanwhile, the rest of the network is constantly adding new blocks ahead of you
7. To succeed, you'd need **more than 50% of the network's total computing power** (a "51% attack") — for Bitcoin, this would require billions of dollars in hardware and electricity

The deeper a transaction is buried in the chain (more **confirmations**), the more computationally expensive it becomes to reverse.

---

## Transaction Lifecycle

Here is exactly what happens from the moment you hit "Send" to when a transaction is considered final:

1. **Create and sign**: You construct a transaction (sender address, recipient address, amount, fee) and sign it with your **private key**
2. **Broadcast**: Your wallet broadcasts the signed transaction to the peer-to-peer network
3. **Mempool**: Unconfirmed transactions sit in the **memory pool (mempool)** of each node, waiting to be picked up by a miner
4. **Block inclusion**: A miner selects transactions from the mempool (typically prioritizing higher fees) and includes them in the next block they're trying to mine
5. **First confirmation**: When a miner successfully mines the block containing your transaction, it receives its **first confirmation**
6. **Additional confirmations**: Each new block added on top of your block is another confirmation
7. **Finality**:
   - **1 confirmation**: acceptable for small amounts
   - **3 confirmations**: typical for most exchanges
   - **6 confirmations**: considered highly secure for Bitcoin; standard for large transfers
   - **Ethereum** is considered final much faster due to its different consensus mechanism

---

## Key Takeaways

> **What to remember from this lesson:**
>
> - A **blockchain** is a distributed ledger — a shared, append-only database maintained by thousands of independent nodes with no central authority.
> - **Hash functions** (SHA-256 in Bitcoin) link blocks together cryptographically; changing any historical data breaks the chain and is detectable immediately.
> - Each block contains a **header** (previous hash, Merkle root, nonce, timestamp) and a **body** (the list of transactions).
> - **Proof of Work** (Bitcoin) secures the chain through computational effort and energy expenditure; **Proof of Stake** (Ethereum, Solana) secures it through economic collateral.
> - Bitcoin's **mining difficulty adjusts** every two weeks to keep block times at ~10 minutes, regardless of how many miners are active.
> - Transactions move from your wallet → **mempool** → a mined block → **confirmations** before they are considered final.
> - **Immutability** comes from the chain structure: altering any historical block requires re-mining every block that follows, making deep attacks economically impossible on large networks.
