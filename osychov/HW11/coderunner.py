# def check_age(age):
#     if age <=0:
#         raise ValueError("Incorrect age")

# try:
#     age = int(input())
#     check_age(age)
#     print(age)
# except:
#     age = int(input())
#     print(age)



################################
    
# def check(login):
#     log = login
#     login = login.lower().replace("-id", " ").replace('id', " ").replace("-", " ")
#     log_ls = login.split(" ")
#     print(login)
#     if log_ls[0] == "admin" or log_ls[0] == "employee":
#             if log_ls[1].isnumeric():
#                 return True
#     else:
#         raise ValueError(f"incorrect login '{log}'")
# print(check("incorrect_login"))
################################


################################

# class MyError(Exception):
#     pass
        
    
# def check_positive(number):
#     if type(number) == str:
#         if number.isdigit():
#             number = int(number)
#     try:  
#         if number > 0 :
#             return f"You input positive number: {float(number)}"
#         if number < 0:
#             return MyError(f"You input negative number: {float(number)}. Try again.")
#     except: 
#         return MyError("Error type: ValueError!")
    
           
# print(check_positive("abc"))

################################
# def divide(numerator :int, denominator:int ):
#     try:
#         result = numerator / denominator
#         return  f"Result is {result}"
#     except ZeroDivisionError:
#         return f"Oops, {numerator}/{denominator}, division by zero is error!!!"
#     except TypeError:
#         return "Value Error! You did not enter a number!"
# print(divide("2", 2))
        
################################

# def check_odd_even(number:int):
#     try:
#         if number % 2 == 0:
#             return "Entered number is even"
#         else:
#             return "Entered number is odd"
#     except TypeError:
#         return "You entered not a number."  
    
# print(check_odd_even("dd"))
            
################################    

# class InputError(Exception):
#     def __init__(self, data) :
#         self.data = data

# def check(text:str):
#     if type(text) !=str:
#         return InputError("Type text error")
#     try: 
#         if len(text) < 3 :
#             return InputError("Short text error")
#         elif len(text) > 15:
#             return InputError("Long text error" )
#         else:
#             return True
#     except:
#         return InputError("Type text error")
    
# def test_input(text):
#     try:
#         print(check(text))
#     except InputError as e :
#         print(e.data)
        
	
	
# test_input({})


################################ 