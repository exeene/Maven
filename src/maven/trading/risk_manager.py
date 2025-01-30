class RiskGuardian:
    def __init__(self, max_drawdown: float = 0.1, position_sizing: float = 0.02):
        """Initialize risk management parameters."""
        self.max_drawdown = max_drawdown  # Max loss before stopping trading
        self.position_sizing = position_sizing  # Fraction of capital per trade
    
    def evaluate_risk(self, account_balance: float, trade_risk: float):
        """Determine if a trade is within acceptable risk limits."""
        max_trade_risk = account_balance * self.position_sizing
        return trade_risk <= max_trade_risk
    
    def should_stop_trading(self, peak_balance: float, current_balance: float):
        """Check if drawdown exceeds allowed threshold."""
        drawdown = (peak_balance - current_balance) / peak_balance
        return drawdown >= self.max_drawdown