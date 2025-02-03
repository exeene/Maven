class TraitBlender:
    def __init__(self):
        self.base_profiles = {
            "quant_queen": {"humor_level": 0.2, "risk_tolerance": 0.7},
            "meme_coin_maven": {"humor_level": 0.8, "risk_tolerance": 0.3}
        }

    def blend_profiles(self, profiles, weights):
        if len(profiles) != len(weights):
            raise ValueError("Number of profiles and weights must match")

        blended_traits = {}
        for trait in self.base_profiles[profiles[0]]:
            blended_traits[trait] = sum(self.base_profiles[p][trait] * w for p, w in zip(profiles, weights))

        return blended_traits