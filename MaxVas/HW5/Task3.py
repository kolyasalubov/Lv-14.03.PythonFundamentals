num = int(input("Enter your number: "))

if num == 0:
    print(1)
elif num < 0:
    print("Factorial is not possible!")
else:
    for i in range(1, num):
        num *= i
    print(num)