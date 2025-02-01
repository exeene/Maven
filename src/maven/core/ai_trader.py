import json
from maven.trading.risk_manager import RiskGuardian
from maven.solana.client import SolanaClient
from maven.llm_integration.openai_client import OpenAIAPI
from maven.core.profile_switcher import ProfileSwitcher
import os

class AITrader:
    def __init__(self, base_profile: str, custom_traits: dict = None):
        """Initialize the AI trading assistant with a personality profile and theme support."""
        self.profile = self.load_profile(base_profile, custom_traits)
        self.risk_manager = RiskGuardian(self.profile["risk_tolerance"])
        self.solana_client = SolanaClient()
        self.openai_api = OpenAIAPI()
        self.profile_switcher = ProfileSwitcher()
        self.theme = self.load_theme("default_theme")
    
    def load_profile(self, profile_name: str, custom_traits: dict = None):
        """Load a predefined or customized personality profile."""
        with open("configs/default_character.json", "r") as file:
            profiles = json.load(file)
        profile = profiles.get(profile_name, {})
        if custom_traits:
            profile.update(custom_traits)
        return profile
    
    def activate_profile(self, new_profile: str, volatility_threshold: float):
        """Dynamically switch personality profile based on market conditions."""
        if self.profile_switcher.should_switch(volatility_threshold):
            self.profile = self.load_profile(new_profile)
            print(f"Switched profile to {new_profile} due to market conditions.")
    
    def get_ai_insight(self, market_data: dict):
        """Fetch trading insights from OpenAI API."""
        prompt = f"Market Analysis: {market_data}. Provide insights based on {self.profile['personality']} personality."
        return self.openai_api.get_response(prompt)
    
    def execute_trade(self, asset: str, amount: float, trade_type: str):
        """Execute buy/sell orders through the Solana client."""
        if self.risk_manager.approve_trade(asset, amount, trade_type):
            return self.solana_client.place_order(asset, amount, trade_type)
        return "Trade rejected by risk management."
    
    def provide_emotional_support(self):
        """Generate emotionally supportive messages during trading turbulence."""
        return f"{self.profile['name']} says: Stay calm, we got this! 💖"
    
    def list_available_themes(self):
        """List available themes from the templates/themes directory."""
        themes_dir = "templates/themes"
        return [f.split(".")[0] for f in os.listdir(themes_dir) if f.endswith(".json")]
    
    def load_theme(self, theme_name: str):
        """Load a theme from the templates/themes directory."""
        theme_path = f"templates/themes/{theme_name}.json"
        if os.path.exists(theme_path):
            with open(theme_path, "r") as file:
                return json.load(file)
        return {}  # Return an empty theme if the file is missing
    
    def apply_theme(self, theme_name: str):
        """Apply a selected theme based on user preference."""
        self.theme = self.load_theme(theme_name)
        print(f"Applied theme: {theme_name}")
