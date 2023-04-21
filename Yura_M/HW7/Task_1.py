# Task1. Write a function that returns the largest number of two
# numbers
# (use DocStrings documentation strings in the function).


def max_number(num1, num2):
    """this function compares two passed values and returns the greater of them"""
    if num1 > num2:
        return num1
    if num1 < num2:
        return num2
    else:
        return "This number is equal"


check = max_number(int(input("enter the number 1: ")),
                   int(input("enter the number 2: ")))

print(check)
