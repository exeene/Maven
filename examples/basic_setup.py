from maven.core.ai_trader import WaifuTrader

trader = WaifuTrader(base_profile="joyful")

trade_result = trader.execute_trade(
    asset="SOL", 
    amount=10.5, 
    trade_type="buy"
)
print(f"Trade Result: {trade_result}")

support_message = trader.provide_emotional_support()
print(support_message)