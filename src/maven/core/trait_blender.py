class TraitBlender:
    """Blends different AI trading profiles to create unique personalities."""
    
    def __init__(self):
        self.base_profiles = {
            "quant_queen": {"humor_level": 0.2, "risk_tolerance": 0.7},
            "meme_coin_maven": {"humor_level": 0.8, "risk_tolerance": 0.3}
        }

    def blend_profiles(self, profiles, weights):
        """Blends multiple profiles based on specified weights."""
        if len(profiles) != len(weights):
            raise ValueError("Number of profiles and weights must match.")

        blended_traits = {trait: 0 for trait in self.base_profiles[profiles[0]]}
        for p, w in zip(profiles, weights):
            for trait in self.base_profiles[p]:
                blended_traits[trait] += self.base_profiles[p][trait] * w
        
        return blended_traits
