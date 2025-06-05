def main():
    renamer()
    
def renamer():
    user_input = input("Enter variable in cameel case: ")
    variable = user_input.split(",")
    for var in variable:
        var= var.strip()
        result = ""
        for char in var:
            if char.isupper():
                result+="_"+char.lower()
            else:
                result+=char
        print("Snake_case: ",result)

main()    
        