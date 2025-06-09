def main():
    plate = input("Enter the plate number: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
    
    
def is_valid(s):
    # Rule 1: Length must be 2–6
    if len(s) < 2 or len(s) > 6:
        return False

    # Rule 2: First two characters must be letters
    if not s[:2].isalpha():
        return False

    # Rule 3: Only alphanumeric characters
    if not s.isalnum():
        return False

    # Rule 4: Digits (if any) must be at the end and not start with '0'
    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] == '0':
                return False  # First digit can't be 0
            if not s[i:].isdigit():
                return False  # All characters after the first digit must be digits only
            break

    return True

        
                
main()