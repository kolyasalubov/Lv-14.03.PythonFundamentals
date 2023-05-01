# QUESTION 1
# The volume of a spherical shell is the difference
# between the enclosed volume of the outer sphere
# and the enclosed volume of the inner sphere:
# Create a function vol_shell() that takes r1 (R) and
# r2 (r) as arguments and returns the volume of a spherical
# shell rounded to the nearest hundredths.

def vol_shell(r1, r2):
    PI = 3.14
    result = round(4 * PI / 3 * (r1**3 - r2**3), 2)
    return result


# QUESTION 2
# Write a function that takes the base and height of a triangle
# and return its area. Round your answer to 2 decimal places

def tri_area(base, height):
    result = round(0.5 * base * height, 2)
    return result


# QUESTION 3
# There is a single operator in Python, capable of providing
# the remainder of a division operation. Two numbers are passed
# as parameters. The first parameter divided by the second
# parameter will have a remainder, possibly zero. Return that value.

def remainder(num1, num2):
    return num1 % num2


# QUESTION 4
# Write a function that takes an integer minutes
# and converts it to seconds.

def convert(minutes):
    return 60 * minutes


# QUESTION 5
# Create a function addition() that takes a number as an argument,
# increments the number by +1, and returns the result.

def addition(number):
    number += 1
    return number
