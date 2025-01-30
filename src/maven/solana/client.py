from solana.rpc.api import Client
from solana.transaction import Transaction
from solana.keypair import Keypair
import json

class SolanaClient:
    def __init__(self, rpc_url="https://api.mainnet-beta.solana.com", config_path="configs/config.json"):
        """Initialize the Solana client with RPC connection."""
        self.client = Client(rpc_url)
        self.load_config(config_path)
    
    def load_config(self, path):
        """Load wallet and other configurations from file."""
        with open(path, "r") as file:
            config = json.load(file)
        self.wallet = Keypair.from_secret_key(bytes(config.get("wallet_secret")))
    
    def get_balance(self, pubkey: str = None):
        """Fetch the SOL balance of a given public key."""
        pubkey = pubkey or self.wallet.public_key
        balance = self.client.get_balance(pubkey)
        return balance["result"]["value"] / 1e9  # Convert lamports to SOL
    
    def send_transaction(self, transaction: Transaction):
        """Send a signed transaction to the Solana network."""
        transaction.sign(self.wallet)
        response = self.client.send_transaction(transaction, self.wallet)
        return response
    
    def get_recent_transactions(self, pubkey: str = None, limit=10):
        """Fetch recent transactions for a given public key."""
        pubkey = pubkey or self.wallet.public_key
        transactions = self.client.get_confirmed_signatures_for_address2(pubkey, limit=limit)
        return transactions