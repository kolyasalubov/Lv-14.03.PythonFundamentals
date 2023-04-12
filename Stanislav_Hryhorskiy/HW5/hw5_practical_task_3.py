"""
*** Practical task 3 ***
Write a script that will calculate the factorial
of the entered number without using recursion.
"""

while True:
    number = input('Enter a non-negative integer: ')
    if number.isdigit():
        break
    else:
        print("You must enter a NON-NEGATIVE INTEGER!!!")

number = int(number)
print()

factorial = 1
if number:
    for var in range(1, number + 1):
        factorial *= var
print(f"The factorial of the entered number: {number}! = {factorial}")
print()

factorial, element = 1, 1
while element <= number:
    factorial *= element
    element += 1
print(f"The factorial of the entered number: {number}! = {factorial}")
