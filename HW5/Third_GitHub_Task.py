# Making factogit rial from user's number

number = int(input("Enter your number:"))
x = 1
for digit in range(2, number+1):
    x *= digit
print(f"Here's your factorial: {number}!=",x)