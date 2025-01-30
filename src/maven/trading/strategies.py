class TradingStrategy:
    def __init__(self, name: str, risk_level: float = 0.5):
        """Initialize a trading strategy with a name and risk level."""
        self.name = name
        self.risk_level = risk_level
    
    def execute(self, market_data):
        """Execute the strategy based on market data."""
        raise NotImplementedError("Subclasses should implement this method")

class MeanReversion(TradingStrategy):
    def __init__(self, risk_level=0.5):
        super().__init__("Mean Reversion", risk_level)
    
    def execute(self, market_data):
        """Simple mean reversion logic."""
        print("Executing Mean Reversion strategy...")
        # Implement trading logic here
        return "Buy" if market_data['price'] < market_data['moving_average'] else "Sell"

class Momentum(TradingStrategy):
    def __init__(self, risk_level=0.7):
        super().__init__("Momentum", risk_level)
    
    def execute(self, market_data):
        """Simple momentum-based trading strategy."""
        print("Executing Momentum strategy...")
        # Implement trading logic here
        return "Buy" if market_data['price_change'] > 0 else "Sell"