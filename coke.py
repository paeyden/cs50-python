def coke(): 
    valid_coins =[25, 10, 5]
    total_amount = 0
    while total_amount<50:
        coin = int(input("Enter the coin: "))
        if coin in valid_coins:
            total_amount+=coin
            if total_amount<50:
                Amount_due= 50-total_amount
                print("Amount due:",Amount_due)
            
        else:
            print("Amount due: ",50-total_amount)
            
    print("Change Owed:",total_amount-50)
    
                
coke()   
    