def twttr():
    text = input("Enter a text: ")
    print(shorten(text))
    

def shorten(word):
    result =""
    omitted_letters =["a","e", "i", "o", "u", "A", "E", "I", "O", "U"]
    
    for char in word:
        if char not in omitted_letters:
            result+=char
            
    return result

if __name__ == "__twttr__":   
    twttr()