def main():
    while True:
        try:
            fraction = input("Enter a fraction: ")
            x, y = fraction.split("/")
            x= int(x)
            y = int(y)
            if x > y:
                break
            if y== 0:
                continue
           
            percent =round((x/y)*100)
            
            if percent <= 1:
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
        