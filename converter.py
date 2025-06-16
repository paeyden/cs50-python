def converter():
    rates = {
        "Dollar":1.00,
        "Euro":1.12,
        "Yen": 0.0071,
        "Pound":1.27
        
    }
    while True:
        try:
            currency = input("Enter the currency: ").title()
            amount= input("Enter the amount: ")
            amount = float(amount)
            if currency not in rates:
                print("Unsupported currency")
                continue
            
            usd = amount*(1/rates[currency])
            print(f"${usd:.2f}")
        except(ValueError, KeyError):
            print("Invalid input. Try again ")
            continue
        except EOFError:
            break
converter()
            