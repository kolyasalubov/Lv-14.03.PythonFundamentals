# Making fibonacci from user's number

number1 = 1
number2 = 0
sequence = [0]
user_number = int(input("Enter your number:"))
for digit in range(user_number):
    digit = number1
    number1 = number1 + number2
    number2 = digit
    sequence.append(digit)

print("Here's your Fibonacci", sequence)
