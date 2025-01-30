import json

class Character:
    def __init__(self, name: str, personality: str, visual: str, config_path="configs/default_character.json"):
        """Initialize a character with predefined attributes or load from config."""
        self.name = name
        self.personality = personality
        self.visual = visual
        self.traits = self.load_character_traits(config_path)
    
    def load_character_traits(self, path: str):
        """Load additional character traits from a configuration file."""
        with open(path, "r") as file:
            characters = json.load(file)
        return characters.get(self.name, {})
    
    def update_trait(self, trait: str, value):
        """Update a specific trait for the character."""
        self.traits[trait] = value
    
    def get_trait(self, trait: str):
        """Retrieve a specific trait value."""
        return self.traits.get(trait, None)
    
    def describe(self):
        """Return a formatted description of the character."""
        return f"Character: {self.name}\nPersonality: {self.personality}\nVisual: {self.visual}\nTraits: {self.traits}"