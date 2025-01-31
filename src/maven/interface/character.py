import json
from pathlib import Path

class AICharacter:
    def __init__(self, name: str, personality: str, visual: str, config_path: str = "configs/default_character.json"):
        """Initialize a character with core attributes and optional configuration"""
        self.name = name
        self.personality = personality
        self.visual = visual
        self.traits = self.load_character_traits(config_path)

    def load_character_traits(self, path: str) -> dict:
        """Load base character traits from configuration file"""
        try:
            with open(path, "r") as file:
                config = json.load(file)
            return config.get(self.name, {})
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def load_profile(self, profile_name: str, custom_traits: dict = None):
        """
        Load a personality profile from templates/character_profiles directory
        Args:
            profile_name: Name of profile file without extension
            custom_traits: Optional dictionary of traits to merge with profile
        """
        profile_path = (
            Path(__file__).parent.parent 
            / "templates" 
            / "character_profiles" 
            / f"{profile_name}.json"
        )
        
        try:
            with open(profile_path, "r") as file:
                profile_data = json.load(file)
            self.traits = profile_data
            
            if custom_traits:
                self.traits.update(custom_traits)
                
        except FileNotFoundError:
            raise ValueError(f"Profile '{profile_name}' not found in templates")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON format in {profile_name}.json")

    @classmethod
    def list_available_profiles(cls) -> list:
        """Return list of available personality profile names"""
        profiles_dir = (
            Path(__file__).parent.parent 
            / "templates" 
            / "character_profiles"
        )
        
        if not profiles_dir.exists():
            return []
            
        return [f.stem for f in profiles_dir.glob("*.json") if f.is_file()]

    def update_trait(self, trait: str, value):
        """Update a specific character trait"""
        self.traits[trait] = value

    def get_trait(self, trait: str):
        """Retrieve a specific trait value"""
        return self.traits.get(trait, None)

    def describe(self) -> str:
        """Generate comprehensive character description"""
        return (
            f"Character: {self.name}\n"
            f"Personality Type: {self.personality}\n"
            f"Visual Style: {self.visual}\n"
            f"Traits: {json.dumps(self.traits, indent=2)}"
        )