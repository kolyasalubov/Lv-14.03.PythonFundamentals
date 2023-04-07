import data

def check_valid_password(inp):
    if len(inp) in range(6, 17):
        for i in inp:
            if i in data.digits:
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
        
        
    
