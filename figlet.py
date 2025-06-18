from pyfiglet import Figlet
import sys
import random

def main():
    figlet = Figlet()
   
    if len(sys.argv) == 1:
       font = random.choice(figlet.getFonts())
       
    elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
        font = sys.argv[2]
        if font not in figlet.getFonts():
            sys.exit("Invalid fonts!")
    else:
        sys.exit("Ivalid usage. Try 'python figlet.py -f slant'")
    
    figlet.setFont(font=font)
    text = input("Input: ")
    print(figlet.renderText(text))
    
main()
        
        