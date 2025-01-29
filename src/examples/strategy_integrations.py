from src.ai_waifu.waifu import AIWaifu

class TradingWaifu(AIWaifu):
    def get_trading_advice(self, strategy_name="default"):
        strategy = self.strategy.get_strategy(strategy_name)
        return f"Remember to: {strategy}"

    def interact(self, user_input):
        # Detect trading-related queries
        if "trading" in user_input.lower() or "invest" in user_input.lower():
            base_prompt = self.character.get_prompt_context()
            strategy_prompt = self.get_trading_advice()
            full_prompt = f"{base_prompt} {strategy_prompt}. User asks: {user_input}. Response:"
            return self.api.generate_response(full_prompt)
        return super().interact(user_input)

def main():
    waifu = TradingWaifu()
    
    print("Trading Advisor Mode (type 'quit' to exit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit']:
            break
        response = waifu.interact(user_input)
        print(f"{waifu.character.name}: {response}")

if __name__ == "__main__":
    main()