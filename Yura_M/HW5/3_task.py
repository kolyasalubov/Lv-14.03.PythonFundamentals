number = int(input("Enter number: "))
b = 1

while number > 0:
    b = number * b
    number -= 1
print(b)
