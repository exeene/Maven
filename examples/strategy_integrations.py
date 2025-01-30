from maven.core.waifu_trader import WaifuTrader
from maven.core.profile_switcher import ProfileSwitcher
import random

trader = WaifuTrader(base_profile="risk-averse")
switcher = ProfileSwitcher(threshold=0.15)

price_history = [random.uniform(80, 120) for _ in range(10)]

volatility = switcher.calculate_volatility(price_history)
print(f"Current Volatility: {volatility:.2%}")

if switcher.should_switch(price_history):
    trader.activate_profile("aggressive", volatility)
    print(f"New Risk Tolerance: {trader.profile['risk_tolerance']}")

print(trader.execute_trade("SOL", 25.0, "buy"))