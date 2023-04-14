even = []
for d in range(1, 11):
    if d % 2 == 0:
        even.append(d)

print(f"Even numbers that are divisible by 2:{even}")

odd = []
for d in range(1, 10):
    if d % 3 == 0 and d % 2 != 0:
        odd.append(d)
print(f"Odd numbers that are divisible by 3:{odd}")

another_num = []
for d in range(1, 10):
    if d % 3 != 0 and d % 2 != 0:
        another_num.append(d)
print(f"Numbers that are not divisible by 2 and 3: {another_num}")