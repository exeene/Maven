from .character import Character
from .strategy import TradingStrategy
from .api import OpenAIAPI

class AIWaifu:
    def __init__(self, config_path="config.json"):
        self.config = load_config(config_path)
        self.character = Character(self.config["character_config"])
        self.strategy = TradingStrategy(self.config["strategy_config"])
        self.api = OpenAIAPI(
            self.config["openai_api_key"],
            self.config["max_tokens"],
            self.config["temperature"]
        )
        
    def interact(self, user_input):
        base_prompt = self.character.get_prompt_context()
        full_prompt = f"{base_prompt} User says: {user_input}. Response: "
        return self.api.generate_response(full_prompt)