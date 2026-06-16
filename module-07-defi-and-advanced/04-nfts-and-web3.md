# Lesson 07.04: NFTs and Web3 — Ownership in the Digital Age

## What Are NFTs?

**NFTs (Non-Fungible Tokens)** are unique digital tokens recorded on a blockchain that certify ownership of a specific digital (or physical) asset. Unlike cryptocurrencies such as BTC or ETH, which are interchangeable, each NFT is one-of-a-kind and cannot be exchanged on a 1-for-1 basis with another NFT.

The word "non-fungible" is the key concept. Understanding it requires comparing it to something that is fungible.

---

## Fungible vs. Non-Fungible: The Core Distinction

**Fungible:** Every unit is identical and interchangeable.
- 1 BTC = 1 BTC. Any Bitcoin in your wallet is worth the same and functions identically to any other Bitcoin.
- A $20 bill = another $20 bill. You can swap them freely without caring which specific bill you have.

**Non-Fungible:** Every unit is unique and not interchangeable.
- **CryptoPunk #7804** is one of the 10,000 CryptoPunks, with a specific combination of attributes (pipe, cap, shades). It has sold for millions and is distinctly not equal to CryptoPunk #1, which has entirely different attributes.
- A signed first-edition book is non-fungible. Even if two copies of the same book exist, one author's signature makes them unequal.

NFTs bring verifiable, unique ownership to the digital world. Before NFTs, there was no cryptographically secure way to assert "I own this specific digital file and there is only one authorized original."

---

## How NFTs Work: ERC-721 Standard

Most NFTs on Ethereum follow the **ERC-721 standard** — a smart contract interface that defines the rules for creating and transferring unique tokens.

Each ERC-721 token has:
- A **unique token ID** (e.g., token #7804)
- An **owner address** (the current holder's Ethereum address)
- A **metadata URI** pointing to a JSON file containing the NFT's name, description, and image URL

The blockchain records every ownership transfer, creating a permanent, public provenance trail. You can verify the entire ownership history of any NFT from its creation to the present moment.

**ERC-1155** is a newer standard supporting both fungible and non-fungible tokens in a single contract, commonly used in gaming where some items are unique (a legendary sword) and others have limited supply (100 health potions).

---

## NFT Use Cases Beyond Digital Art

While digital art dominated early NFT narratives, the technology has far broader applications:

### Digital Art and Collectibles
Digital artists mint their work as NFTs, enabling proof of original ownership and automatic royalties (typically 5-10%) on secondary sales via smart contracts.

### Gaming Items
In-game items as NFTs are player-owned assets that exist outside the game developer's servers. Games like Axie Infinity (Ronin network) pioneered this model. If the game shuts down, the NFTs remain in your wallet — unlike traditional in-game items that vanish with the game.

### Music Rights
Artists like Kings of Leon have released albums as NFTs, granting holders access to exclusive experiences or a share of streaming royalties. NFTs can replace or supplement complex traditional music rights management.

### Real-World Asset Tokenization
Physical assets — real estate deeds, luxury goods, fine art — can be tokenized as NFTs, enabling fractional ownership, easier transfer, and instant secondary market liquidity. This is an area of significant institutional interest.

### Identity and Credentials
Academic degrees, professional certifications, and event tickets issued as NFTs are verifiable, unforgeable, and transferable. **POAP (Proof of Attendance Protocol)** NFTs are already used to record event participation on-chain.

---

## NFT Market History: Boom, Bust, and Relevance

### The 2021 Boom

- **March 2021:** Digital artist Beeple sells "Everydays: The First 5000 Days" at Christie's for **$69.3 million** — the third-highest price ever achieved by a living artist at the time.
- **Bored Ape Yacht Club (BAYC)** launches in April 2021 at 0.08 ETH (~$190). Floor price eventually exceeded 100 ETH (~$350,000+). Owners included Justin Bieber, Eminem, and Paris Hilton.
- Total NFT market trading volume reached approximately **$25 billion** in 2021.

### The 2022-2023 Bust

The NFT market crashed alongside the broader crypto bear market. Many collections that sold for tens of thousands of dollars saw floor prices drop 90-99%. Wash trading — artificially inflating apparent volume by trading with yourself — was exposed as rampant across platforms.

### Current Landscape

Focus has shifted toward utility-based NFTs (gaming assets, credentials, real-world asset tokenization) rather than pure speculative art. Trading volume has consolidated on **Blur** (professional traders) and **OpenSea** (retail users).

---

## How to Value NFTs

NFTs lack fundamental metrics like stocks (earnings, cash flows, P/E ratios). Valuation is largely subjective, driven by:

- **Rarity:** How uncommon are the specific trait combinations within a collection? Rarity scoring tools rank NFTs by trait frequency. A CryptoPunk with multiple rare attributes commands a premium.
- **Utility:** Does the NFT provide tangible benefits — exclusive access, governance rights, in-game power, revenue share?
- **Community strength:** Active Discord, engaged Twitter following, and developer momentum sustain demand. A dead community precedes floor price collapse.
- **Creator reputation:** A credible, established artist or team commands a premium. Anonymous creators with no track record carry higher risk.
- **Provenance:** Celebrity ownership history (the Eminem or Justin Bieber Bored Ape) adds a premium in collector markets.
- **Collection size:** Smaller collections of higher quality often hold value better than large 10,000-item PFP (profile picture) collections in a down market.

**The honest reality:** NFT valuation is highly speculative. The vast majority of NFT collections bought at peak prices in 2021 are now essentially worthless. Treat most NFT purchases as speculative bets on cultural relevance, not investments with predictable returns.

---

## Web3: The User-Owned Internet Vision

**Web3** is a framework for a new phase of the internet where users own their data, identity, and digital assets, enabled by blockchain technology.

### The Evolution of the Web

- **Web1 (1991-2004):** Read-only. Static pages, no user contribution.
- **Web2 (2004-present):** Read-write. Social media and user-generated content — but your data is owned by corporations (Facebook, Google). The user is the product.
- **Web3 (emerging):** Read-write-own. Users control their own data via cryptographic keys. Platforms are governed by token holders, not corporations.

### Key Web3 Concepts

- **Self-sovereign identity:** Your identity is tied to your wallet address, not a corporate username database. You control access.
- **Data ownership:** Instead of platforms harvesting your data, you own it and choose who may access it.
- **Tokenized ownership:** Contributions to protocols and communities are compensated with tokens that carry real economic value and governance rights.

---

## DApps: Decentralized Applications

**DApps (Decentralized Applications)** are applications whose core logic runs on a blockchain via smart contracts rather than on corporate servers. The front-end may still be a traditional website, but it connects to the blockchain for all transactions and state changes.

**How a DApp connects to your wallet:**
1. You visit a DApp (e.g., app.uniswap.org)
2. The site prompts you to connect your **MetaMask** or other Web3 wallet
3. MetaMask injects your wallet address into the site
4. When you execute a transaction, MetaMask signs it with your private key locally
5. The signed transaction is broadcast to the Ethereum network and executed by the smart contract

Your private key never leaves your device. The DApp cannot access your funds — it can only propose transactions that you must explicitly approve in MetaMask.

---

## Risks in the NFT and Web3 Space

- **Market illiquidity:** You may be unable to sell an NFT quickly at a fair price. Thin markets mean wide bid-ask spreads and potentially weeks to find a buyer.
- **Copyright ambiguity:** Buying an NFT does not automatically convey copyright over the underlying artwork in most jurisdictions. Legal frameworks are still developing.
- **Wash trading:** Sellers trade with themselves to create the appearance of demand. Volume statistics can be deeply misleading.
- **Phishing and wallet drainers:** Malicious smart contracts disguised as legitimate NFT mints or airdrops can drain your entire wallet if you approve them. Never sign transactions you don't understand fully.
- **Speculative failure rate:** The vast majority of NFT collections lose value over time. Only the top collections maintain meaningful long-term floors.

---

## Getting Started: Primary and Secondary Markets

- **OpenSea (opensea.io):** The original NFT marketplace. Largest selection, user-friendly, supports Ethereum, Polygon, and other chains.
- **Blur (blur.io):** Professional NFT trading platform favored by active traders. Aggregates listings across marketplaces, enables portfolio-wide bidding, offers BLUR token rewards.
- **Magic Eden:** Dominant on Solana, expanding multi-chain. Lower fees and faster transactions for Solana-based NFTs.

**For beginners:** Start by exploring without buying. Connect MetaMask to OpenSea, browse collections, and study which attributes drive rarity premiums before committing capital.

---

> ## Key Takeaways
>
> - **NFTs are non-fungible tokens** — unique on-chain ownership certificates. CryptoPunk #7804 ≠ CryptoPunk #1; 1 BTC = 1 BTC (fungible).
> - **ERC-721** is the Ethereum standard for NFTs: each token has a unique ID, owner address, and permanent transfer history on-chain.
> - NFT use cases extend well beyond art: **gaming items, music rights, real estate tokenization, digital identity, and event credentials** all benefit from NFT infrastructure.
> - The 2021 boom featured Beeple's **$69.3M Christie's sale** and Bored Apes reaching 100+ ETH floors; the 2022 crash erased most NFT value.
> - NFT valuation depends on **rarity, utility, community strength, creator reputation, and provenance** — there are no cash flow fundamentals.
> - **Web3** envisions user-owned internet: self-sovereign identity, data ownership, and tokenized community participation replacing Web2's corporate data extraction model.
> - **DApps** connect to MetaMask; your private key never leaves your device — you must explicitly approve every transaction.
> - Core risks: illiquidity, copyright ambiguity, wash trading, phishing/wallet drainers, and the very high speculative failure rate of most collections.
> - Start on **OpenSea** (retail, broad selection) or **Blur** (professional trading with volume incentives).

## What Is a Non-Fungible Token?

Fungibility means interchangeability. One US dollar bill is worth exactly the same as any other US dollar bill — they are fungible. One Bitcoin is equivalent to any other Bitcoin. ERC-20 tokens on Ethereum follow this model: every unit of a given token is identical.

An NFT, by contrast, is unique. The ERC-721 token standard defines tokens where each unit has a distinct identifier and can carry distinct metadata — typically a link to an image, video, audio file, or other digital asset. Two tokens in the same ERC-721 contract are not interchangeable; token ID #1 is different from token ID #2, and the market may price them very differently based on their attributes.

**ERC-721 vs ERC-20 at a glance:**

| Property | ERC-20 | ERC-721 |
|---|---|---|
| Fungibility | Fungible (identical) | Non-fungible (unique) |
| Divisibility | Divisible | Indivisible (whole units) |
| Primary use | Currency, governance | Digital ownership, collectibles |
| Token IDs | Shared balance | Unique per token |

A newer standard, ERC-1155, is a hybrid that supports both fungible and non-fungible tokens in a single contract — commonly used in gaming where a player might hold 500 identical arrows (fungible) and one legendary sword (non-fungible).

## How On-Chain Ownership Works

Owning an NFT means controlling the wallet address recorded as the owner in the smart contract's on-chain ledger. This ownership record is public, immutable, and verifiable by anyone. It cannot be forged or deleted. Transferring ownership updates the on-chain record — no intermediary required.

What the NFT typically does *not* contain is the underlying media file itself. Storing images directly on-chain would be prohibitively expensive. Instead, most NFTs store a URI pointing to metadata hosted on IPFS (a decentralized file system) or, in weaker implementations, a centralized server. If that server goes offline, the image disappears — the token remains, but it points to nothing. This "off-chain metadata" problem is an acknowledged weakness in many NFT projects.

Some projects have pursued fully on-chain storage, encoding the image directly in the smart contract (often as SVG). These are considered more durable, though the richness of the media is limited by gas costs.

## Use Cases Beyond Digital Art

**Digital art and collectibles:** The use case that drove mainstream awareness. Artists like Beeple and collections like CryptoPunks and Bored Ape Yacht Club established NFTs as a new category of digital art ownership. Collectors pay for provable scarcity and verifiable provenance.

**Gaming:** In-game items — weapons, characters, land parcels — represented as NFTs can be owned, traded, or used across compatible games. Games like Axie Infinity and Illuvium pioneered this model. True cross-game interoperability remains largely theoretical, but player-owned economies have launched successfully.

**Music:** Artists including 3LAU, Kings of Leon, and Royal have sold music as NFTs, granting buyers royalty rights, exclusive access, or simply a verifiable ownership record. This model offers artists a way to capture more value directly from fans, bypassing traditional label structures.

**Identity and credentials:** Soulbound tokens (SBTs), a concept popularized by Ethereum co-founder Vitalik Buterin, are non-transferable NFTs. They could represent academic degrees, professional certifications, or reputation scores — credentials that belong to a person and cannot be sold.

**Real-world asset tokenization:** Physical assets — real estate, fine art, luxury goods — can be represented as NFTs, enabling fractional ownership and global liquidity. This is an active area of experimentation with real regulatory complexity.

## How NFT Markets Work

The two dominant NFT marketplaces are **OpenSea** and **Blur**.

**OpenSea** is the historically dominant general marketplace, supporting a wide range of collections across multiple blockchains. It takes a percentage fee on each sale and passes a portion to the original creator as a royalty.

**Blur** launched in 2022 targeting professional traders with lower fees, faster interfaces, and token incentives for high-volume activity. It quickly captured significant market share and intensified the royalty debate — Blur made creator royalties optional, pressuring OpenSea to follow suit. The royalty wars significantly reduced artist income from secondary sales.

NFT prices are set by supply and demand. Floor price — the lowest current asking price for any token in a collection — is the standard measure of a collection's market value. Volume (total USD traded in a period) indicates how actively a collection is trading.

## Valuation Challenges

Valuing NFTs is genuinely difficult. Unlike stocks (future cash flows) or bonds (fixed coupons), most NFTs produce no income. Their value derives from:

- **Community and social status:** Holding a Bored Ape signals membership in an exclusive group, which carries social and networking value.
- **Scarcity and provenance:** Limited supply plus a verifiable, prestigious history of ownership.
- **Utility:** Access to events, games, or governance rights built around the NFT.
- **Brand and narrative:** Some collections build IP, merchandise, and media franchises around their tokens.

All of these value drivers are subjective and reflexive — they depend on continued belief in the community. Collections that lose narrative momentum can lose 90%+ of their floor price rapidly. Wash trading (a seller buying their own NFT to inflate volume and price) has been documented extensively and distorts market signals.

## Web3: The User-Owned Internet

Web3 is a broader vision for the next evolution of the internet. The framing goes:

- **Web1** (1990s–2000s): Read-only. Static pages, no user accounts.
- **Web2** (2000s–present): Read-write. Platforms like Facebook, YouTube, and Twitter let users create content — but the platforms own the data, the relationships, and the monetization.
- **Web3** (emerging): Read-write-own. Users control their digital assets, data, and identity through wallets and cryptographic keys. Platforms are replaced by protocols that no single company controls.

In the Web3 model, your social graph, your game inventory, your creative work, and your financial history are owned by you — stored in your wallet — and portable across applications. An NFT can be your avatar on one platform, your game character on another, and your concert ticket on a third.

Critics note that current Web3 applications often fail to deliver on this vision: many still rely on centralized infrastructure, governance is frequently concentrated among large token holders, and the user experience remains too complex for mainstream adoption. The gap between the vision and the current reality is wide — but the architectural primitives exist.

---

## Key Takeaways

- NFTs use the ERC-721 standard to create unique, individually identified tokens on a blockchain — distinct from fungible ERC-20 tokens.
- On-chain ownership is verifiable and immutable, but the media files most NFTs point to are usually stored off-chain, introducing durability risk.
- Real use cases span digital art, gaming items, music rights, identity credentials, and real-world asset tokenization.
- OpenSea and Blur are the dominant NFT marketplaces; Blur's rise compressed creator royalties industry-wide.
- NFT valuation is inherently subjective — community strength, scarcity, utility, and narrative all drive prices, making wash trading and rapid value collapse common.
- Web3 describes a user-owned internet model where crypto wallets replace platform accounts, giving users control over their data, assets, and identity — an ambitious vision still far from full realization.
