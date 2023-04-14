num = int(input("Enter your number: "))
factorial = 1
if num < 0:
    print("No factorial for negative numbers")
elif num == 0:
    print("Factorial = 1")
else:
    for i in range(1, num + 1):
        factorial=factorial*i
    print("Factorial =", factorial)