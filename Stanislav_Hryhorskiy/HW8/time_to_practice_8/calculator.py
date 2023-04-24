# *** Time to practice 8 ***
# Create a module with functions of addition, subtraction,
# multiplication, division. And in another module - calculator.py, it is
# necessary to ask the user what action he wants to perform and
# with what numbers and perform the necessary actions.

import functions

if __name__ == "__main__":
    functions.get_text_menu()
    operation_number = int(input('Enter the number of the math operation: '))
    first_number = float(input('Enter the first number: X = '))
    second_number = float(input('Enter the second number: Y = '))
    functions.get_math_operation(operation_number, first_number, second_number)
