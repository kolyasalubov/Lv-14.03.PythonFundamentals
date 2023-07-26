f = int(input("Write your factorial:"))

value = 1
if f < 0:
    print("You can't use this number.")
elif f == 0:
    value = 1
else:
    for digit in range(1, f+1):
        value = value * digit
print(value)
