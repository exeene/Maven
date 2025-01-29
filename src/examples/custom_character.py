from src.ai_waifu.waifu import AIWaifu
from src.ai_waifu.character import Character

def main():
    # Load custom character configuration
    custom_character = Character("examples/custom_character.json")
    
    # Initialize waifu with default config then override character
    waifu = AIWaifu()
    waifu.character = custom_character
    
    print(f"Custom Character: {custom_character.name} (type 'quit' to exit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit']:
            break
        response = waifu.interact(user_input)
        print(f"{custom_character.name}: {response}")

if __name__ == "__main__":
    main()