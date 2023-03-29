"""
Write a script, which of the two entered numbers will determine which of them is
more and which is less. Take into account the case of equality of numbers.
"""

number_1, number_2 = map(float, input("Enter a two numbers separated by space: ").split())

if number_1 == number_2:
    print(f"Both entered numbers are equal: "
          f"number_1 = {number_1} = number_2 {number_2}")
elif number_1 > number_2:
    print(f"The first number is greater than the second: "
          f"number_1 = {number_1} > number_2 = {number_2}")
else:
    print(f"The second number is greater than the first: "
          f"number_2 = {number_2} > number_1 = {number_1}")


"""
Write a script that will check whether the entered number 
is even or odd and display the appropriate message.
"""

number = int(input("Enter an integer: "))
if number % 2:
    print(f"Entered number {number} is odd")
else:
    print(f"Entered number {number} is even")

number = int(input("Enter an integer: "))
print(f"Entered number {number} is odd" if number % 2 else f"Entered number {number} is even")
