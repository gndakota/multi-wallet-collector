# Multi-Wallet Collector 🚀

A Python script to automatically collect funds from multiple wallets and transfer them to a main wallet.

## Features:
✅ Supports multiple Ethereum wallets  
✅ Automatically checks balances and sends funds  
✅ Optimized gas usage  
✅ Handles transactions in batches  

## Installation:
**1. Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_GITHUB_USERNAME/multi-wallet-collector.git
   cd multi-wallet-collector

**2. Install dependencies:**
pip install web3 python-dotenv

**Configuration:**
1. Add your wallet details to wallets.json:
[
  {"address": "0xYourWalletAddress1", "private_key": "0xYourPrivateKey1"},
  {"address": "0xYourWalletAddress2", "private_key": "0xYourPrivateKey2"}
]

**2. Set up the .env file:**
Create a .env file by copying .env.example
Add your Infura URL and Main Wallet Address:
INFURA_URL=https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID
MAIN_WALLET=0xYourMainWalletAddress

**Usage:**
Run the script:
python collect_funds_wallets.py

This script will check the balance of each wallet in wallets.json and transfer funds (above the minimum threshold) to the MAIN_WALLET.
