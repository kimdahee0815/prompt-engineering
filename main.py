import os
from dotenv import load_dotenv

def is_loaded(name):
    return bool(os.getenv(name))

def main():
    print("Hello from prompt-basic!")

load_dotenv()

if __name__ == "__main__":
    main()
    print(f"OPENAI_API_KEY loaded: {is_loaded('OPENAI_API_KEY')}")
    print(f"ANTHROPIC_API_KEY loaded: {is_loaded('ANTHROPIC_API_KEY')}")
