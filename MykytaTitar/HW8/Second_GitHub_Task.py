import re


while True:
    users_password = input("Please make your password:")
    letters = re.findall("[a-z]", users_password)
    letters = len(letters)
    upper_letters = re.findall("[A-Z]", users_password)
    upper_letters = len(upper_letters)
    digits = re.findall("[0-9]", users_password)
    digits = len(digits)
    symbols = re.findall("[$#@]", users_password)
    symbols = len(symbols)
    if len(users_password) >= 6:
        if letters >= 1 and upper_letters >= 1:
            if digits >= 1 and symbols >= 1:
                print("Your password is valid. Enjoy our product!")
                break
    else:
        print("Sorry your password is invalid. Try again.")

