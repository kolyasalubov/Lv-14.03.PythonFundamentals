"""
*** Practical task 2 ***
Write a script that checks the login that the user enters.
If the login is "First", then greet the users. If the login is
different, send an error message. (need to use loop while)
"""

VALID_LOGIN = "First".lower()

while True:
    user_login = input("Enter your login: ").lower()
    if user_login != VALID_LOGIN:
        print("Error: the user login was entered incorrectly!")
    else:
        print("Congratulations! You have entered the login correctly.")
        break
