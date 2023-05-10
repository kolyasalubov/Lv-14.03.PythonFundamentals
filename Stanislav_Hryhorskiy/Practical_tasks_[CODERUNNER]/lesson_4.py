# QUESTION 1
# Write a function that takes a credit card number
# and only displays the last four characters.
# The rest of the card number must be replaced by ************
# If the length of the number is less than 16 symbols
# the function returns "Invalid card"

def card_hide(card):
    if len(str(card)) != 16:
        return "Invalid card"
    return str(card).replace(str(card)[:12], 12*'*')


# QUESTION 2
# Given two numbers, return True if the sum of both
# numbers is less than 100. Otherwise, return False.

def less_than_100(num1, num2):
    return num1 + num2 < 100


# QUESTION 3
# Create a function that takes a number as an argument and returns
# negative of that number. Return negative numbers without any change.

def return_negative(number):
    return -abs(number)


# QUESTION 4
# Write a function that returns True if k^k == n for input (n, k)
# and return False otherwise. The ^ operator refers to exponentiation
# operation **, not the bitwise XOR operation.

def k_to_k(num1, num2):
    return num1 == num2 ** num2


# QUESTION 5
# Create a function that returns True if an integer
# is evenly divisible by 5, and False otherwise.

def divisible_by_five(number):
    return not number % 5


# QUESTION 6
# Write a function that stutters a word as if someone is struggling
# to read it. The first two letters are repeated twice with
# an ellipsis ... , and then the word is pronounced with a question mark ?.
# If the input is less than two characters long, the function returns "oh...".

def stutter(word):
    if len(word) < 2:
        return "oh..."
    return f"{word[:2]}...{word[:2]}...{word}?"


# QUESTION 7
# Create a function that takes two arguments.
# Both arguments are integers, a and b.
# Return True if one of them is 10 or if their sum is 10.

def makes10(num1, num2):
    return 10 in (num1, num2) or num1 + num2 == 10
