import data
import re

def check_valid_password(inp):
    if len(inp) in range(6, 17):
        for i in data.digits:
            if i in inp:
                break
        else:
            print("You should have a number in your password!")
            exit()
        for i in data.symbols:
            if i in inp:
                break
        else:
            print("You should have one of these signes in your password (@, #, $)")
            exit()
        for i in data.alphabet:
            if i in inp:
                break
        else:
            print("You should have one letter between [a-z]")
            exit()
        for i in data.alphabet_upper:
            if i in inp:
                break
        else:
            print("You should have one letter between [A-Z]")
            exit()
        print("Password is valid and good!!!")
    else:
        print("Your password's length shoud be from 6 to 16!")
        exit()
        
        
def check_valid_with_re(inp):
    if len(inp) in range(6, 17):
        result_digits = re.search("[0-9]", inp)
        result_symbols = re.search("[#, 4, @]", inp)
        result_alphabet = re.search("[a-z]", inp)
        result_alphabet_upper = re.search("[A-Z]", inp)
        if result_digits is None:
            print("You should have a number in your password!")
            exit()
        elif result_symbols is None:
            print("You should have one of these signes in your password (@, #, $)")
            exit()
        elif result_alphabet is None:
            print("You should have one letter between [a-z]")
            exit()
        elif result_alphabet_upper is None:
            print("You should have one letter between [A-Z]")
            exit()
        else:
            print("Password is valid and good!!!")
    else:
        print("Your password's length shoud be from 6 to 16!")
        exit()
def check_implementation(password):
    if len(password) < 6 or len(password) > 16:
        return False

    if not re.search(r'\d', password):    #decimal digit [0-9]
        return False
    if not re.search(r'[@#$]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[A-Z]', password):
        return False


    return True