from .utils import load_config

class Character:
    def __init__(self, config_path):
        self.config = load_config(config_path)
        self.name = self.config.get("name", "AI Waifu")
        self.personality = self.config.get("personality", "helpful and friendly")
        self.interaction_style = self.config.get("interaction_style", "casual")

    def get_prompt_context(self):
        return f"{self.name} is {self.personality} and interacts in a {self.interaction_style} manner. "