import json

class PersonalityMatrix:
    def __init__(self, profile_name: str, custom_traits: dict = None, config_path="configs/default_character.json"):
        """Initialize personality with predefined or custom traits."""
        self.profile = self.load_profile(profile_name, config_path)
        if custom_traits:
            self.profile.update(custom_traits)
    
    def load_profile(self, profile_name: str, path: str):
        """Load a personality profile from the config file."""
        with open(path, "r") as file:
            profiles = json.load(file)
        return profiles.get(profile_name, {})
    
    def blend_personalities(self, base_profile: str, additional_profile: str, blend_ratio: float = 0.5):
        """Blend traits from two profiles to create a hybrid personality."""
        base = self.load_profile(base_profile, "configs/default_character.json")
        additional = self.load_profile(additional_profile, "configs/default_character.json")
        blended = {key: (base.get(key, 0) * (1 - blend_ratio) + additional.get(key, 0) * blend_ratio) 
                   for key in set(base) | set(additional)}
        self.profile.update(blended)
        return self.profile
    
    def get_trait(self, trait: str):
        """Retrieve a specific trait value."""
        return self.profile.get(trait, None)
    
    def set_trait(self, trait: str, value):
        """Update or add a trait value."""
        self.profile[trait] = value