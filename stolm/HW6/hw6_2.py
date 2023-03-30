database = []

login = input("Welcome to our site!\n"
              "To get started, enter your login: ")

while True:
    if login == "First":
        print(f"Hello, {login}! Glad to see you again!")
        break 
    else:
        print("Error! No user found with this username!\n")
        login = input("Enter your login again! : ")
