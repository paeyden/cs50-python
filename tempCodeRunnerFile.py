def interpreter():
    x, y, z = input("Enter an expression: ").split()
    operation = y
    num1=int(x)
    num2 = int(z)
    if operation == "+":
        result=num1 + num2
        
    elif operation=="-":
        result = num1 - num2 
       
    elif operation=="*":
        result=num1 * num2 
        
    elif operation=="/":
        result=num1/num2
    else:
        print("Enter a valid operator")
        return
    print(f"{result:.1f}")   
    
    
interpreter()    