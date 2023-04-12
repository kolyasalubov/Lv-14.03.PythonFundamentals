def check_pass(password):
    sym_arr = ["$", "#", "@"]
    check_letter = lambda s: any(i.islower() for i in s) and any(i.isupper() for i in s)

    isDigit = False
    isSym = False
    isUpperAndLower = False

    for char in password:
        if char.isdigit():
            isDigit = True
        elif char in sym_arr:
            isSym = True   
            
    if check_letter(password):
        isUpperAndLower = True

    if isDigit and isSym and isUpperAndLower and 6<=len(password)<=16:
        return "Your password is valid"
    else:
        return "Your password isn't valid!"


if __name__ == "__main__":
    password = input("Enter your password: ")
    print(check_pass(password))
