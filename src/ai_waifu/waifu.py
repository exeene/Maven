from typing import Optional, Dict, Any
from .character import Character
from .strategy import TradingStrategy
from .api import OpenAIAPI
from .solana import SolanaClient
from .utils import load_config

class AIWaifu:
    def __init__(self, config_path: str = "config.json"):
        self.config = load_config(config_path)
        self._validate_config()
        
        self.character = Character(self.config["character_config"])
        self.strategy = TradingStrategy(self.config["strategy_config"])
        self.api = OpenAIAPI(
            api_key=self.config["openai_api_key"],
            max_tokens=self.config.get("max_tokens", 150),
            temperature=self.config.get("temperature", 0.7),
            model=self.config.get("model", "gpt-3.5-turbo")
        )
        self.solana = SolanaClient(
            self.config.get("solana_network", "https://api.mainnet-beta.solana.com")
        )

    def _validate_config(self) -> None:
        """Validate critical configuration values"""
        required_keys = ["openai_api_key", "character_config", "strategy_config"]
        missing = [k for k in required_keys if k not in self.config]
        if missing:
            raise ValueError(f"Missing required config keys: {missing}")

    def interact(self, user_input: str) -> Optional[str]:
        """Handle user interaction with input validation"""
        if not isinstance(user_input, str) or len(user_input) == 0:
            raise ValueError("Invalid user input")
        
        base_prompt = self.character.get_prompt_context()
        full_prompt = f"{base_prompt} User says: {user_input}. Response: "
        return self.api.generate_response(full_prompt)