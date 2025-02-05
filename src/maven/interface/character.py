import json
from pathlib import Path
from typing import Dict, Optional, List

class CharacterConfigError(Exception):
    """Custom exception for character configuration errors."""
    pass

class AICharacter:
    def __init__(self, name: str, personality: str, visual: str, config_path: str = "configs/default_character.json"):
        """Initialize a character with core attributes and optional configuration."""
        self.name = name
        self.personality = personality
        self.visual = visual
        self.traits = self._load_character_traits(config_path)
    
    def _load_character_traits(self, path: str) -> Dict[str, str]:
        """Load base character traits from configuration file."""
        try:
            with open(path, "r", encoding="utf-8") as file:
                config = json.load(file)
            return config.get(self.name, {})
        except FileNotFoundError:
            raise CharacterConfigError(f"Configuration file not found: {path}")
        except json.JSONDecodeError:
            raise CharacterConfigError(f"Invalid JSON format in {path}")
    
    def load_profile(self, profile_name: str, custom_traits: Optional[Dict[str, str]] = None) -> None:
        """Load a personality profile from templates."""
        profile_path = Path(__file__).parent.parent / "templates" / "character_profiles" / f"{profile_name}.json"
        
        try:
            with open(profile_path, "r", encoding="utf-8") as file:
                profile_data = json.load(file)
            self.traits = profile_data
            if custom_traits:
                self.traits.update(custom_traits)
        except FileNotFoundError:
            raise CharacterConfigError(f"Profile '{profile_name}' not found.")
        except json.JSONDecodeError:
            raise CharacterConfigError(f"Invalid JSON format in {profile_name}.json")
    
    @classmethod
    def list_available_profiles(cls) -> List[str]:
        """Return list of available personality profile names."""
        profiles_dir = Path(__file__).parent.parent / "templates" / "character_profiles"
        return [f.stem for f in profiles_dir.glob("*.json") if f.is_file()] if profiles_dir.exists() else []
    
    def update_trait(self, trait: str, value: str) -> None:
        """Update a specific character trait."""
        self.traits[trait] = value
    
    def get_trait(self, trait: str) -> Optional[str]:
        """Retrieve a specific trait value."""
        return self.traits.get(trait)

    def describe(self) -> str:
        """Generate a detailed character description."""
        return (
            f"Character: {self.name}\n"
            f"Personality Type: {self.personality}\n"
            f"Visual Style: {self.visual}\n"
            f"Traits:\n{json.dumps(self.traits, indent=2)}"
        )

    def save_character_state(self, output_path: str) -> None:
        """Save the current state of the character to a JSON file."""
        state = {
            "name": self.name,
            "personality": self.personality,
            "visual": self.visual,
            "traits": self.traits
        }
        try:
            with open(output_path, "w", encoding="utf-8") as file:
                json.dump(state, file, indent=4)
        except IOError as e:
            raise CharacterConfigError(f"Failed to save character state: {e}")

    def load_character_state(self, input_path: str) -> None:
        """Load a previously saved character state from a JSON file."""
        try:
            with open(input_path, "r", encoding="utf-8") as file:
                state = json.load(file)
            self.name = state.get("name", self.name)
            self.personality = state.get("personality", self.personality)
            self.visual = state.get("visual", self.visual)
            self.traits = state.get("traits", self.traits)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            raise CharacterConfigError(f"Failed to load character state: {e}")
