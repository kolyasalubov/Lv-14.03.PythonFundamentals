fct = int(input("Enter your number: "))
s = 1
if fct == 0 or fct == 1:
    print(f"{fct}! =", 1)
else:
    for i in range(1, fct + 1):
        s *= i
    print(f"{fct}! =", s)