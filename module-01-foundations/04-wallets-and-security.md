# Lesson 4: Wallets and Security

## Introduction

In traditional finance, your bank holds your money. If you forget your password, they reset it. If someone steals your card, the bank reverses the charge. Crypto offers none of these safety nets by default — and that is both its greatest strength and its most dangerous feature.

**In crypto, whoever controls the private key controls the funds. Full stop.**

This lesson will teach you everything you need to know to store crypto safely, understand how wallets actually work, and avoid the mistakes that have caused countless people to permanently lose their assets.

---

## Hot Wallets vs. Cold Wallets

The fundamental distinction in crypto storage comes down to **internet connectivity**.

### Hot Wallets
- **Definition**: A wallet whose private keys are stored on a device connected to the internet
- **Examples**: MetaMask (browser extension), Trust Wallet (mobile), Phantom (Solana), Coinbase Wallet
- **Advantages**: Convenient, instant access, free, required for DeFi interaction
- **Disadvantages**: Exposed to online threats — malware, phishing, browser exploits, exchange hacks
- **Best for**: Amounts you're actively trading or using in DeFi. Think of it like a physical wallet in your pocket — you keep spending money there, not your life savings.

### Cold Wallets
- **Definition**: A wallet whose private keys are stored offline — never touching the internet
- **Examples**: Ledger Nano X/S Plus, Trezor Model T/One, paper wallets
- **Advantages**: Immune to remote hacking, secure for long-term storage
- **Disadvantages**: Less convenient, costs money, requires careful physical security
- **Best for**: Long-term holdings ("**cold storage**"). Think of it as a safe deposit box — not for daily use, but for serious security.

**The golden rule**: Only keep on a hot wallet what you can afford to lose. Move significant holdings to cold storage.

---

## Software Wallets: Setup and Use

### MetaMask
The most widely used Ethereum wallet, available as a browser extension (Chrome, Firefox, Brave) and mobile app.

- **What it supports**: Ethereum and all EVM-compatible chains (Polygon, Arbitrum, Optimism, Avalanche C-Chain, BNB Chain, etc.)
- **Setup**: Download from **metamask.io only** (never search in app stores — fake MetaMask apps are a major attack vector). Create a new wallet. Write down your **12-word seed phrase** on paper, offline. Set a strong password.
- **Key feature**: Connects to dApps (decentralized applications) via your browser. When you click "Connect Wallet" on Uniswap, MetaMask handles the authentication.
- **Risk**: Browser-based, so it's exposed to browser vulnerabilities, malicious browser extensions, and phishing sites

### Trust Wallet
A mobile wallet supporting hundreds of blockchains — BTC, ETH, SOL, BNB Chain, Polygon, and more.

- **Owned by Binance** but operates as a non-custodial wallet (Binance cannot access your funds)
- Good for users who want multi-chain support in one app
- Built-in dApp browser for DeFi access on mobile

### Phantom
The dominant wallet for the **Solana** ecosystem. Available as a browser extension and mobile app.

- Supports SOL, SPL tokens (Solana's token standard), and Solana NFTs
- Has expanded to support Ethereum and Bitcoin as well
- Clean, fast interface optimized for Solana's high-throughput environment

---

## Hardware Wallets: The Gold Standard for Security

A **hardware wallet** is a physical device — roughly the size of a USB drive — that stores your private keys in an isolated, tamper-resistant chip called a **Secure Element**. The keys are generated and stored on the device and **never leave it unencrypted**.

### How They Work
1. You connect the hardware wallet to your computer via USB or Bluetooth
2. When you want to sign a transaction, the transaction data is sent to the device
3. The device displays the transaction details on its own screen (separate from your potentially-compromised computer)
4. **You physically confirm the transaction on the device** by pressing a button
5. The device signs the transaction internally and returns only the signed output — your private key never touches your computer

This design means that even if your computer is infected with malware, an attacker cannot steal your keys or sign fraudulent transactions without physical access to your device.

### Ledger
- **Models**: Nano S Plus (~$79), Nano X (~$149, Bluetooth, mobile compatible)
- Supports 5,500+ cryptocurrencies
- Uses a **closed-source Secure Element** — the security chip firmware is proprietary
- **Controversy**: In 2023, Ledger introduced "Ledger Recover," a paid service that optionally splits and backs up your seed phrase to third-party servers. The crypto community reacted sharply — it proved the device *could* extract the seed phrase, which contradicted earlier security claims. The service is opt-in, but it changed how many people think about Ledger's security model.

### Trezor
- **Models**: Trezor One (~$69), Trezor Model T (~$179, touchscreen)
- Fully **open-source** hardware and firmware — anyone can audit the code
- Does not use a proprietary Secure Element — instead relies on its open-source architecture and physical security
- Supports fewer coins than Ledger but is trusted by many security-conscious users

**Bottom line**: Either Ledger or Trezor is dramatically safer than any hot wallet for significant holdings. Buy directly from the manufacturer — never from Amazon or eBay (risk of tampered devices).

---

## Seed Phrases (BIP-39): Your Master Key

When you set up any non-custodial wallet, you are given a **seed phrase** (also called a **recovery phrase** or **mnemonic phrase**) — a sequence of **12 or 24 common English words**.

### How It Works
- This sequence of words is generated from a pool of **2,048 predefined words** (the BIP-39 wordlist)
- The words encode a **large random number** called **entropy**
- This entropy is fed through a derivation algorithm (**BIP-32/BIP-44**) to generate a virtually unlimited number of private/public key pairs
- **Every single wallet address** you ever create from that seed phrase can be regenerated from those same words — on any compatible wallet software

### What This Means in Practice
- Lose your hardware wallet? Buy a new one, enter your seed phrase, and all your funds are accessible again
- Your phone is stolen? Enter your seed phrase into a new device
- Your seed phrase is compromised? **Every account derived from it is at risk — permanently**

### How to Store Your Seed Phrase
- Write it **by hand** on paper — never type it, screenshot it, or store it digitally
- Store in a **fireproof and waterproof** location (a fireproof safe)
- Consider a **metal backup** (companies like Cryptosteel make stainless steel plates for engraving seed words — fireproof, waterproof, and crush-proof)
- **Never store it in a cloud service** (Google Drive, Dropbox, iCloud, email)
- Consider splitting storage locations — but this increases complexity

---

## Private Keys vs. Public Keys: The Mailbox Analogy

Crypto uses **asymmetric cryptography** (public-key cryptography). You have two mathematically linked keys:

### The Mailbox Analogy
- Your **public key** (and the wallet address derived from it) is like your **mailbox address** — you share it freely so people can send you mail (crypto)
- Your **private key** is like the **key to the mailbox** — only you have it, and it's the only thing that allows you to take mail out (spend funds)
- Anyone with the key can open the mailbox. If you lose the key, a locksmith can't help — the funds are gone forever.

### Technical Details
- A **private key** is a 256-bit random number, typically represented as a 64-character hexadecimal string
- A **public key** is derived from the private key using elliptic curve cryptography (specifically **secp256k1** in Bitcoin and Ethereum)
- A **wallet address** is derived from the public key (via SHA-256 and RIPEMD-160 in Bitcoin; via Keccak-256 in Ethereum) — it's a shorter, checksum-protected representation
- The math is **one-way**: you can go from private key → public key → address, but not backwards

---

## Wallet Addresses: What They Are

A wallet address is what you share when you want to receive crypto. It looks like this:

- **Bitcoin**: `bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh`
- **Ethereum**: `0x742d35Cc6634C0532925a3b844Bc454e4438f44e`
- **Solana**: `7EcDhSYGxXyscszYEp35KHN8vvw3svAuLKTzXwCFLtV`

Key points:
- Addresses are **case-sensitive in some networks** (Ethereum has a checksum encoding in mixed case)
- Different blockchains use **completely different address formats** — never send ETH to a BTC address
- An address can receive funds from anyone, but only the holder of the corresponding private key can spend them
- One seed phrase generates **millions of addresses** — it's best practice to use a new address for each transaction for privacy

---

## Critical Security Rules

These are non-negotiable:

### Never Share Your Seed Phrase
- **No legitimate wallet provider, exchange, customer support agent, or "admin" will ever ask for your seed phrase**
- Anyone who asks for it is trying to steal your funds. This is the #1 attack vector in crypto.
- Not even Ledger or Trezor support staff needs your seed phrase to help you

### Always Verify Addresses
- Before sending any transaction, **verify the recipient address character by character** — at minimum the first 6 and last 6 characters
- On a hardware wallet, **verify the address on the device screen**, not just your computer screen (more on clipboard hijacking below)

### Use 2FA Everywhere
- Enable **two-factor authentication** on every exchange and email account related to crypto
- Use an **authenticator app** (Google Authenticator, Authy) rather than SMS — SIM swap attacks are common
- SMS 2FA is better than nothing but vulnerable; app-based 2FA is significantly more secure

### Keep Software Updated
- Wallet firmware updates patch security vulnerabilities. Update promptly.

---

## Common Attack Vectors

### Phishing
- Fake websites that look identical to MetaMask, Coinbase, Uniswap, etc.
- Delivered via Google ads, fake Discord links, email, Twitter DMs
- **Defense**: Bookmark official sites. Never click links from DMs. Always check the URL bar carefully.

### Clipboard Hijacking
- Malware silently monitors your clipboard and replaces crypto addresses you copy with the attacker's address
- You copy `0x742d35Cc...`, you paste `0xAttacker...`, you send funds to the wrong address
- **Defense**: Always verify addresses on your hardware wallet screen. Check the first and last 6 characters after pasting.

### Fake Apps
- Fake MetaMask, Trust Wallet, Ledger Live apps in app stores
- They capture your seed phrase when you enter it during "setup"
- **Defense**: Only download from official websites. On mobile, verify the developer name in the app store listing.

### Malicious Smart Contract Approvals
- DeFi interactions require you to **approve** a smart contract to spend your tokens
- Malicious contracts can be approved to drain your entire wallet balance
- **Defense**: Use tools like **revoke.cash** to audit and revoke unnecessary token approvals. Never blindly approve unlimited spending.

### Social Engineering ("Discord Admin" scams)
- Attackers pose as moderators/admins in official project Discord servers
- They DM you with "urgent" security issues requiring you to "verify" your wallet
- **Defense**: Real admins never DM first. Disable DMs from server members.

---

## Custodial vs. Non-Custodial: "Not Your Keys, Not Your Coins"

### Custodial Wallets
- A third party (an exchange like Coinbase, Binance, Kraken) holds your private keys on your behalf
- You access your funds via a username/password login
- **Advantages**: Easy recovery, customer support, familiar interface
- **Disadvantages**: You don't actually own the crypto — you own an IOU. The exchange can freeze withdrawals, go bankrupt (FTX collapsed in November 2022, trapping billions in customer funds), get hacked, or be pressured by regulators.

### Non-Custodial Wallets
- **You hold your own private keys** (MetaMask, Ledger, Trezor, Trust Wallet in self-custody mode)
- No one can freeze your funds or deny you access
- **Disadvantages**: Full responsibility — if you lose your seed phrase, no one can help you recover

### The FTX Lesson
In November 2022, **FTX** — then the third-largest crypto exchange in the world — collapsed in 72 hours due to fraud. Over **$8 billion** in customer funds were lost. Customers who had moved their crypto off the exchange to self-custody wallets lost nothing. Those who trusted FTX with custody lost everything.

The phrase "**not your keys, not your coins**" is not a slogan — it's a hard lesson learned by millions of people.

**Best practice**: Use exchanges for trading. **Withdraw your holdings to a hardware wallet** for any amount you want to keep long-term.

---

## Key Takeaways

> **What to remember from this lesson:**
>
> - **Hot wallets** (MetaMask, Phantom, Trust Wallet) are convenient but internet-connected and vulnerable. Use them for amounts you're actively trading.
> - **Cold wallets** (Ledger, Trezor) store private keys offline, making remote theft impossible. Use them for significant long-term holdings.
> - Your **seed phrase** (12 or 24 BIP-39 words) is the master key to all accounts in a wallet. Store it offline, in writing, in a secure physical location. Never share it with anyone.
> - The **private key → public key → address** relationship is one-way. Your address can receive funds; only your private key can spend them.
> - Always **verify addresses** on your hardware wallet screen before confirming. Clipboard hijacking is real.
> - Enable **authenticator app-based 2FA** on all exchange accounts. Avoid SMS-based 2FA.
> - **Custodial accounts** (exchanges) carry counterparty risk — FTX proved that even "reputable" exchanges can collapse. Withdraw long-term holdings to self-custody.
> - "**Not your keys, not your coins**" is the most important phrase in crypto security.
