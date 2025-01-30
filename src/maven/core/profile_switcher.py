class ProfileSwitcher:
    def __init__(self, threshold: float = 0.5):
        """Initialize the profile switcher with a volatility threshold."""
        self.threshold = threshold
    
    def calculate_volatility(self, price_history: list):
        """Calculate market volatility based on price history."""
        if len(price_history) < 2:
            return 0
        
        price_changes = [abs(price_history[i] - price_history[i - 1]) / price_history[i - 1] 
                         for i in range(1, len(price_history))]
        return sum(price_changes) / len(price_changes)
    
    def should_switch(self, price_history: list):
        """Determine if the AI should switch profiles based on volatility."""
        volatility = self.calculate_volatility(price_history)
        return volatility >= self.threshold