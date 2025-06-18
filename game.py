import random


def main():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                break
        except ValueError:
            continue
        
        
    while True:
       try:
            number = random.randint(1,level)
            user_input = int(input("Guess: "))
            if user_input < number:
                print("Too small")
            elif user_input > number:
                print("Too large!")
            else:
                print("Just right!")
                return
       except ValueError:
           continue

main()