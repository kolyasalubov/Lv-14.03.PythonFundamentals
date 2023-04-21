# Task2. Write a script that checks the login that the user enters.
# If the login is "First", then greet the users. If the login is
# different, send an error message.
# (need to use loop while)


def check(login):
    first_login = 'Yura'
    while login == first_login:
        print(f"Hello {first_login}")
        break
    else:
        print("TypeError: You have entered an invalid username, please try again ")


enter = check(input("Enter your login: "))
