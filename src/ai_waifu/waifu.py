import logging
from .character import Character
from .strategy import TradingStrategy
from .api import OpenAIAPI
from .utils import load_config  # Ensure load_config is properly imported

class AIWaifu:
    """
    AIWaifu serves as an interactive AI character with trading strategies
    and OpenAI-based conversation capabilities.
    """
    
    def __init__(self, config_path: str = "config.json") -> None:
        """
        Initializes AIWaifu with configurations for character, strategy, and OpenAI API.

        :param config_path: Path to the configuration JSON file.
        """
        try:
            self.config = load_config(config_path)
            self.character = Character(self.config.get("character_config", {}))
            self.strategy = TradingStrategy(self.config.get("strategy_config", {}))
            self.api = OpenAIAPI(
                api_key=self.config.get("openai_api_key", ""),
                max_tokens=self.config.get("max_tokens", 100),
                temperature=self.config.get("temperature", 0.7)
            )
        except Exception as e:
            logging.exception(f"Failed to initialize AIWaifu: {e}")
            raise

    def interact(self, user_input: str) -> str:
        """
        Generates a response based on user input.

        :param user_input: The input text from the user.
        :return: AI-generated response.
        """
        try:
            base_prompt = self.character.get_prompt_context()
            full_prompt = f"{base_prompt} User says: {user_input}. Response: "
            return self.api.generate_response(full_prompt)
        except Exception as e:
            logging.exception(f"Error generating response: {e}")
            return "I'm sorry, but I encountered an error while generating a response."
