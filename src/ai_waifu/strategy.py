from .utils import load_config

class TradingStrategy:
    def __init__(self, config_path):
        self.strategies = load_config(config_path)
        
    def get_strategy(self, strategy_name):
        return self.strategies.get(strategy_name, "No strategy found")