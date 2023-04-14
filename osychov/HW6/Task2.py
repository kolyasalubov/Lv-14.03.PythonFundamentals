def login_is_correct():
   login = {"Alex"}
   input_login = input("Write your login: ")
   while input_login not in login:
       print("Incorrect login! Try again!")
       login_is_correct()
   else:
       print("Hy,", input_login)
       exit()
login_is_correct()
    








# def user_is_correct():
#     login_password = {"alex2005": "alex123456"}
#     input_login = input("Write your login: ")
#     input_password = input("Write your password: ")


#     while input_login not in login_password.keys() and input_password not in login_password.values():
#         print("Incorrect login or password, try again! ")
#         user_is_correct()
#     else:
#         print("Hy", login_password)
# user_is_correct()
