# SecureVault 🛡️

A lightweight, zero-dependency Python utility for cryptographic password hashing and verification using industry-standard key derivation.

## What It Does
SecureVault takes plaintext credentials and derives cryptographically secure password hashes using `PBKDF2-HMAC` with `SHA-256`, applied over 100,000 iterations. Every hash is paired with a unique, cryptographically random 32-byte salt generated via `os.urandom(32)` to defeat rainbow table attacks and precomputed dictionary lookups.

## Why I Built It
Most beginners store credentials in plaintext or rely on insecure single-pass hashing like standard MD5/SHA-1. I built SecureVault to understand key derivation functions (KDFs) at the implementation level and create a zero-dependency reference tool that developers can drop into Python CLI workflows without pulling in bloated third-party dependencies.

## Tech Stack
- **Language:** Python 3.x
- **Core Modules:** `hashlib` (PBKDF2-HMAC), `os` (CSPRNG via `os.urandom`)
- **Dependencies:** None (Pure Standard Library)

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/PS282006/secure-vault.git
   cd secure-vault
   ```
2. Run the CLI:
   ```bash
   python3 vault.py
   ```
3. Enter a password when prompted to inspect the generated salt and derived key output.
