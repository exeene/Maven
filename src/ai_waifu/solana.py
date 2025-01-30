from solders.keypair import Keypair
from solders.pubkey import Pubkey
from solana.rpc.api import Client
from typing import Optional, Union
from .utils import error_handler

class SolanaClient:
    def __init__(self, network: str = "https://api.mainnet-beta.solana.com"):
        self.client = Client(network)
        self.keypair: Optional[Keypair] = None

    @error_handler
    def set_keypair(self, private_key: bytes) -> None:
        """Initialize keypair from bytes"""
        self.keypair = Keypair.from_bytes(private_key)

    @error_handler
    def get_balance(self, pubkey: Optional[Union[str, Pubkey]] = None) -> Optional[int]:
        """Get SOL balance for a public key"""
        if pubkey is None:
            if self.keypair is None:
                raise ValueError("No keypair specified")
            pubkey = self.keypair.pubkey()
        
        if isinstance(pubkey, str):
            pubkey = Pubkey.from_string(pubkey)
            
        return self.client.get_balance(pubkey).value