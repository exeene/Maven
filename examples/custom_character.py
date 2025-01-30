from maven.core.waifu_trader import WaifuTrader

custom_traits = {
    "name": "CryptoChan",
    "risk_tolerance": "aggressive",
    "catchphrase": "Yatta! Let's moon this! 🚀",
    "emotional_support": [
        "HODL the line, senpai!",
        "This dip is just a temporary setback!"
    ]
}

trader = WaifuTrader(
    base_profile="default",
    custom_traits=custom_traits
)

print(f"Trader Name: {trader.profile['name']}")
print(trader.provide_emotional_support())