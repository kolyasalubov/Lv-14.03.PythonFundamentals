"""
*** Practical task 3 ***
Interchange the values of two variables
without using the third variable.
"""

variable_1 = input('Enter the first variable: ')
variable_2 = input('Enter the second variable: ')
print(f"\nThe values of the first and second variables are entered:\n"
      f"\t- variable_1 = {variable_1};\n"
      f"\t- variable_2 = {variable_2}.\n")

variable_1, variable_2 = variable_2, variable_1

print(f"The values of the first and second variables are interchanged:\n"
      f"\t- variable_1 = {variable_1};\n"
      f"\t- variable_2 = {variable_2}.")
