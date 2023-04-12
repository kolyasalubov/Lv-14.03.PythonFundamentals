login = input("Enter your login: ")
while login != 'First':
    login = input("Invalid login, try again: ")
else:
    print(f"Welcome, {login}")