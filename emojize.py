import emoji


def main():
    
     user_input = input("Input: ").strip()
     emojized_text = emoji.emojize(user_input, language="alias")
     print(f"Output: {emojized_text}")
    
main()
        