# QUESTION 1
# Write python module. All your code will be wrote in file module.py.
# If we run pyhon module.py it must print "Hello world!" in terminal.
# But if we import this file we must be able to call function
# say_greeting, which obtain one argument name and print in terminal
# "Hello {name}".
# Note that your code will be callad once in first test case.
# For example:
# Test	                          Result
# import module                   Hello User
# module.say_greeting("User")

def say_greeting(name):
    print(f"Hello {name}")


if __name__ == "__main__":
    say_greeting("world!")


# QUESTION 2
# We have file module.py with such code:
# FREEZING_POINT = None
# BOILING_POINT = None
# def print_water_state(temperature):
#       if temperature <= FREEZING_POINT:
#              print("Solid")
#       elif FREEZING_POINT < temperature < BOILING_POINT:
#              print("Liquid")
#       else:
#              print("Gas")
#
# Use this module in your script to print the state of the water
# if its temperature is determined with input from the user.
# We assume that the freezing point is 0 degrees and the boiling
# point is 100 degrees.
# Do not use any function definitions or if statements in your code.

import module

module.FREEZING_POINT = 0
module.BOILING_POINT = 100

temperature = int(input())

module.print_water_state(temperature)
