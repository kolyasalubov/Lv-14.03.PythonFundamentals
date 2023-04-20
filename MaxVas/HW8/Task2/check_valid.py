import re
        
def check_pass(user_input):
    if len(user_input) in range(6, 17):
        if not re.search("[0-9]", user_input):
            print("You must have a number")
            exit()
        elif not re.search("[@, #, $]", user_input):
            print("You must have @ or # or $")
            exit()
        elif not re.search("[a-z]", user_input):
            print("You must have one of [a-z]")
            exit()
        elif not re.search("[A-Z]", user_input):
            print("You must have one of [A-Z]")
            exit()
        else:
            print("Nice, your password is valid")
    else:
        print("Your password's must be from 6 to 16 characters!")
        exit()

user_input = input("Enter the password: ")
check_pass(user_input)