def camel():
    camel_case = input("Enter a word written in camel case: ").strip()
    result = ""
    for s in camel_case:
        if s.isupper():
            result+="_"+s.lower()
        else:
            result+=s
    print("snake_case:",result)         
            
        
        
camel()