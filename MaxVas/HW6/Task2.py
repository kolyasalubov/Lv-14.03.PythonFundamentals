user_input = input("Enter your login: ")
login = "First"

while user_input != login:
    user_input = input("Login incorrect! Try again: ")
else:
    print(f"Greetings @{login}, glad you are here!")