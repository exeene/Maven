from typing import Dict, Any
from pathlib import Path
from .utils import load_config

class Character:
    PERSONALITIES = {
        "tsundere": {"traits": ["blunt", "secretly caring"], "style": "informal"},
        "kuudere": {"traits": ["calm", "analytical"], "style": "formal"},
        # Add more personality templates
    }

    def __init__(self, config_path: str):
        if not Path(config_path).exists():
            raise FileNotFoundError(f"Character config {config_path} not found")
            
        self.config = load_config(config_path)
        self._apply_personality_template()
        
        self.name: str = self.config.get("name", "AI Waifu")
        self.personality: str = self.config.get("personality", "helpful and friendly")
        self.interaction_style: str = self.config.get("interaction_style", "casual")

    def _apply_personality_template(self) -> None:
        """Apply predefined personality template if specified"""
        if "template" in self.config:
            template = self.PERSONALITIES.get(self.config["template"], {})
            self.config = {**template, **self.config}

    def get_prompt_context(self) -> str:
        return f"{self.name} ({self.personality}) interacting in {self.interaction_style} style: "