from src.ai_waifu.waifu import AIWaifu

def main():
    # Initialize with default config
    waifu = AIWaifu()
    
    print("AI Waifu Basic Setup (type 'quit' to exit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit']:
            break
        response = waifu.interact(user_input)
        print(f"{waifu.character.name}: {response}")

if __name__ == "__main__":
    main()