import json
import logging
import os
from pathlib import Path
from typing import Any, Dict, Optional

from maven.trading.risk_manager import RiskGuardian
from maven.solana.client import SolanaClient
from maven.llm_integration.openai_client import OpenAIAPI
from maven.core.profile_switcher import ProfileSwitcher

# Configure module-level logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # Adjust the logging level as needed


class AITrader:
    def __init__(self, base_profile: str, custom_traits: Optional[Dict[str, Any]] = None):
        """
        Initialize the AI trading assistant with a personality profile and theme support.
        """
        self.configs_path = Path("configs")
        self.templates_path = Path("templates/themes")
        self.theme_cache: Dict[str, Dict[str, Any]] = {}

        self.profile = self.load_profile(base_profile, custom_traits)
        self.risk_manager = RiskGuardian(self.profile.get("risk_tolerance", 0.5))
        self.solana_client = SolanaClient()
        self.openai_api = OpenAIAPI()
        self.profile_switcher = ProfileSwitcher()
        self.theme = self.load_theme("default_theme")

    def load_profile(self, profile_name: str, custom_traits: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Load a predefined or customized personality profile.
        Raises a FileNotFoundError if the profile file is missing.
        """
        profile_file = self.configs_path / "default_character.json"
        if not profile_file.exists():
            logger.error(f"Profile file not found: {profile_file}")
            raise FileNotFoundError(f"Missing configuration file: {profile_file}")

        try:
            with profile_file.open("r", encoding="utf-8") as file:
                profiles = json.load(file)
            profile = profiles.get(profile_name, {})
            if not profile:
                logger.warning(f"Profile '{profile_name}' not found in {profile_file}. Using empty profile.")
            if custom_traits:
                profile.update(custom_traits)
            logger.debug(f"Loaded profile: {profile_name} with traits: {profile}")
            return profile
        except json.JSONDecodeError as e:
            logger.error(f"Error decoding JSON from {profile_file}: {e}")
            raise

    def activate_profile(self, new_profile: str, price_history: list):
        """
        Dynamically switch personality profile based on market conditions.
        :param new_profile: Name of the new profile to activate.
        :param price_history: List of historical price data to assess volatility.
        """
        if self.profile_switcher.should_switch(price_history):
            self.profile = self.load_profile(new_profile)
            logger.info(f"Switched profile to {new_profile} due to market volatility.")
        else:
            logger.debug("Profile switch not required based on current market conditions.")

    def get_ai_insight(self, market_data: Dict[str, Any]) -> str:
        """
        Fetch trading insights from the OpenAI API.
        :param market_data: Dictionary containing market data.
        :return: AI-generated trading insight.
        """
        personality = self.profile.get("personality", "default")
        prompt = f"Market Analysis: {market_data}. Provide insights based on a {personality} personality."
        logger.debug(f"Sending prompt to OpenAI API: {prompt}")
        return self.openai_api.get_response(prompt)

    def execute_trade(self, asset: str, amount: float, trade_type: str) -> Any:
        """
        Execute buy/sell orders through the Solana client.
        :param asset: The asset to trade.
        :param amount: The amount to trade.
        :param trade_type: 'buy' or 'sell'.
        :return: Response from the Solana client or a risk management rejection message.
        """
        if self.risk_manager.approve_trade(asset, amount, trade_type):
            logger.info(f"Trade approved for {trade_type} of {amount} {asset}.")
            return self.solana_client.place_order(asset, amount, trade_type)
        logger.warning("Trade rejected by risk management.")
        return "Trade rejected by risk management."

    def simulate_trade(self, asset: str, amount: float, trade_type: str) -> str:
        """
        Simulate a trade without executing it. This new feature allows for dry-run analysis of trade decisions.
        :param asset: The asset to simulate trading.
        :param amount: The amount to trade.
        :param trade_type: 'buy' or 'sell'.
        :return: A string message simulating the trade outcome.
        """
        if self.risk_manager.approve_trade(asset, amount, trade_type):
            simulation_result = (f"Simulated {trade_type} order for {amount} units of {asset} "
                                 f"would be executed successfully.")
            logger.info(simulation_result)
            return simulation_result
        simulation_result = "Simulated trade rejected by risk management."
        logger.info(simulation_result)
        return simulation_result

    def provide_emotional_support(self) -> str:
        """
        Generate emotionally supportive messages during trading turbulence.
        :return: A supportive message.
        """
        name = self.profile.get("name", "AITrader")
        message = f"{name} says: Stay calm, we got this! 💖"
        logger.debug(message)
        return message

    def list_available_themes(self) -> list:
        """
        List available themes from the templates/themes directory.
        :return: A list of theme names (without extension).
        """
        if not self.templates_path.exists():
            logger.warning(f"Themes directory does not exist: {self.templates_path}")
            return []
        themes = [p.stem for p in self.templates_path.glob("*.json")]
        logger.debug(f"Available themes: {themes}")
        return themes

    def load_theme(self, theme_name: str) -> Dict[str, Any]:
        """
        Load a theme from the templates/themes directory with caching.
        :param theme_name: Name of the theme (without extension).
        :return: A dictionary representing the theme.
        """
        if theme_name in self.theme_cache:
            logger.debug(f"Loaded theme '{theme_name}' from cache.")
            return self.theme_cache[theme_name]

        theme_path = self.templates_path / f"{theme_name}.json"
        if theme_path.exists():
            try:
                with theme_path.open("r", encoding="utf-8") as file:
                    theme = json.load(file)
                self.theme_cache[theme_name] = theme
                logger.debug(f"Loaded theme from file: {theme_name}")
                return theme
            except json.JSONDecodeError as e:
                logger.error(f"Error decoding theme JSON from {theme_path}: {e}")
        else:
            logger.warning(f"Theme file not found: {theme_path}")
        return {}

    def apply_theme(self, theme_name: str) -> None:
        """
        Apply a selected theme based on user preference.
        :param theme_name: The name of the theme to apply.
        """
        self.theme = self.load_theme(theme_name)
        logger.info(f"Applied theme: {theme_name}")
