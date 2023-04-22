# *** Task 1 ***
# Write a program that prompts the user
# to enter an integer and determines whether
# the number is even or odd, taking into account
# the case of entering incorrect data.

try:
    number = int(input("Enter a natural number: "))
except ValueError as error:
    print(f"ValueError: {error}")
else:
    if number % 2:
        print(f"Entered number {number} is odd.")
    else:
        print(f"Entered number {number} is even.")


# *** Task 2 ***
# Write a program to calculate the divide
# of two numbers entered by the user sequentially
# through a comma, to predict the case of division
# by zero, cases of syntactic errors and cases
# of other exceptional situations. Use the else
# and finally  blocks.


try:
    first_number, second_number = input("Enter two numbers, separated by comma: ").split(',')
    result = float(first_number) / float(second_number)
except ValueError as error:
    print(f"ValueError: {error}")
except ZeroDivisionError as error:
    print(f"ZeroDivisionError: {error}")
except:
    print("Oops! Something went wrong")
else:
    print(f"The divide of two numbers ({float(first_number)}; "
          f"{float(second_number)}) entered by the user is {result}.")
finally:
    print("The program is complete")
