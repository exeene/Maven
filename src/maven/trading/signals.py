class SignalGenerator:
    def __init__(self, signals_config):
        self.signals_config = signals_config

    def generate_signals(self, market_data):
        signals = []
        for signal_name, conditions in self.signals_config.items():
            if all(self.check_condition(market_data, **cond) for cond in conditions):
                signals.append(signal_name)
        return signals

    def check_condition(self, market_data, indicator, threshold, operator):
        value = getattr(market_data, indicator)
        if operator == ">":
            return value > threshold
        elif operator == "<":
            return value < threshold
        # Add more operators as needed
        return False