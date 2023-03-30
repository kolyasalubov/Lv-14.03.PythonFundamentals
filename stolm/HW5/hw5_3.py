number = int(input("Enter your number: "))
number_copy = number

if number_copy >= 0:
    fact = 1
    while number_copy != 0:
        fact *= number_copy
        number_copy -= 1
    print(f"The factorial of a {number} is {fact}")
else:
    print(f"The factorial of your number {number} "
          "can't be determined. Most likely, it is less than 0!")
    