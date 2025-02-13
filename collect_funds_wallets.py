import json
import time
import os
from web3 import Web3
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Connect to Ethereum (or another EVM-compatible network)
INFURA_URL = os.getenv("INFURA_URL")  # Replace with your RPC URL
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Main wallet to collect funds
MAIN_WALLET = os.getenv("MAIN_WALLET")

# Minimum balance threshold for transfers (e.g., 0.01 ETH)
MIN_BALANCE = 0.01

# Load wallet list
with open("wallets.json", "r") as file:
    wallets = json.load(file)

def get_balance(address):
    balance_wei = web3.eth.get_balance(address)
    return web3.from_wei(balance_wei, 'ether')

def send_transaction(private_key, from_address, to_address, amount):
    nonce = web3.eth.get_transaction_count(from_address)
    gas_price = web3.eth.gas_price
    
    transaction = {
        'to': to_address,
        'value': web3.to_wei(amount, 'ether'),
        'gas': 21000,
        'gasPrice': gas_price,
        'nonce': nonce,
        'chainId': web3.eth.chain_id
    }
    
    signed_tx = web3.eth.account.sign_transaction(transaction, private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return tx_hash.hex()

def collect_funds():
    for wallet in wallets:
        address = wallet["address"]
        private_key = wallet["private_key"]
        
        balance = get_balance(address)
        print(f"{address}: {balance} ETH")
        
        if balance > MIN_BALANCE:
            try:
                tx_hash = send_transaction(private_key, address, MAIN_WALLET, balance - 0.001)  # Deduct gas fees
                print(f"Sent {balance - 0.001} ETH from {address} to {MAIN_WALLET} | TX: {tx_hash}")
            except Exception as e:
                print(f"Error sending from {address}: {e}")
        
        time.sleep(1)  # Avoid hitting rate limits

if __name__ == "__main__":
    collect_funds()
