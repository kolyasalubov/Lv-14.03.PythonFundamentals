# QUESTION 1
# Write code inside function check.
# This function must check logins of some workers.
# We have 2 roles: there are "admin" and "employee",
# each login must contain role and id.
# Id is any natural number. Id and role may be separated
# by "-" or "-id" or "id". If function check obtain incorrect
# data (as example 'abc') it needs to raise ValueError with
# message "incorrect login 'abc'". Note that all data may be
# case-insensitive.

import re

pattern = re.compile(r"(?:admin|employee)+(?:-)*(?:id)*(?:\d)+",
                     flags=re.I)


def check(login: str):
    if pattern.match(login):
        return True
    else:
        raise ValueError(f"incorrect login '{login}'")


# QUESTION 2
# Write the function check_positive(number)whose input parameter
# is a number. The function checks whether the set number is positive
# or negative: in the case of a positive number the function should be
# displayed the corresponding message - "You input positive number:
# input parameter of function"; in the case of a negative parameter
# the function should return the exception to your own class MyError
# and displayed the corresponding message. "You input negative number:
# input parameter of function. Try again."; in the case of incorrect
# data the function should be displayed the message -
# "Error type: ValueError!"

class MyError(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return self.data


def check_positive(number):
    try:
        result = float(number)
        if result < 0:
            raise MyError(f"You input negative number: {result}. Try again.")
    except ValueError:
        return "Error type: ValueError!"
    except MyError as error:
        return error
    else:
        return f"You input positive number: {result}"


# QUESTION 3
# Write your code bellow to create custom Error named InputError
# and function check. The error must save description of error
# in data attribute. In data of error must be written:
# "Short text error" if length of string less than 3,
# "Long text error" if length of string more than 15,
# "Type text error" if we try to check not string.
# Your function check will be called from function test_input
# as shown on screenshot.

class InputError(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return self.data


def check(text):
    if not isinstance(text, str):
        raise InputError("Type text error")
    else:
        if len(text) < 3:
            raise InputError("Short text error")
        elif len(text) > 15:
            raise InputError("Long text error")
    return True


# QUESTION 4
# Write the function check_odd_even (number) whose input parameter
# is an integer number. The function checks whether the set number
# is even or odd:
# in the case of an even number the function should be displayed
# the corresponding message - "Entered number is even";
# in the case of an odd number the function should be displayed
# the corresponding message - "Entered number is odd";
# in the case of incorrect data the function should be displayed
# the message - "You entered not a number."
# Note: in the function you must use the try except construct.

def check_odd_even(number):
    try:
        result = int(number) % 2
    except ValueError:
        return f"You entered not a number."
    else:
        if result:
            return "Entered number is odd"
        else:
            return "Entered number is even"


# QUESTION 5
# With help input obtain from user his age. Age must be natural number.
# If user try input incorrect value ask him again. If user typed correct
# age print this value. Do not use if in your code, but you can use
# already created function check_age for validation.

while True:
    try:
        age = int(input())
        check_age(age)
    except ValueError:
        continue
    else:
        print(age)
        break


# QUESTION 6
# Write the function divide(numerator, denominator) the two input
# parameters of which are numbers. The function returns the result
# of dividing two numbers:
# in case of correct data the function should be displayed
# the corresponding message – "Result is numerator / denominator"
# in the case of division by zero the function should be displayed
# the corresponding message – "Oops, numerator / denominator,
# division by zero is error!!!".
# in the case of incorrect data the function should be displayed
# the message –"Value Error! You did not enter a number!"
# Note: in the function you must use the try except construct.

def divide(numerator, denominator):
    try:
        if isinstance(numerator, int) and isinstance(denominator, int):
            result = numerator / denominator
        else:
            raise ValueError
    except ZeroDivisionError:
        return f"Oops, {numerator}/{denominator}, division by zero is error!!!"
    except ValueError:
        return f"Value Error! You did not enter a number!"
    else:
        return f"Result is {result}"
