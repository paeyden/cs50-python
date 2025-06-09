def twttr():
    omitted_letters =["a","e", "i", "o", "u", "A", "E", "I", "O", "U"]
    text = input("Enter a text: ")
    result =""
    for char in text:
        if char not in omitted_letters:
            result+=char
            
    print(result,end="")
twttr()    
    