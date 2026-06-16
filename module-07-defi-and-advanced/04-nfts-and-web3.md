# NFTs and Web3

Non-Fungible Tokens and the broader concept of Web3 represent one of the most discussed — and most misunderstood — evolutions in blockchain technology. Between 2021 and 2022, NFTs generated billions of dollars in trading volume and attracted mainstream media attention, celebrity endorsements, and serious institutional interest. They also attracted speculation, fraud, and intense skepticism. Cutting through the hype requires understanding the underlying mechanics, the genuine use cases, and the honest valuation challenges these assets present.

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
