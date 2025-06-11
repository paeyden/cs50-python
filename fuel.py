def main():
    while True:
        try:
            fraction = input("Enter a fraction: ")
            x, y = fraction.split("/")
            if y== 0 or  x > y:
                continue
            x= int(x)
            y = int(y)
            percent =round((x/y)*100)
            
            if percent < 1:
                print("E")
            elif percent>=99:
                print("F")
            
            else:
                print(f"{percent}%")
            break
            
        except ValueError: 
            continue
        
        except ZeroDivisionError:
            continue
main()
        