
n = input("Write a four-digit natural number:")

mult = 1

for digit in n:
    mult = int(digit) * mult

print(mult)


revers_n = n[::-1]

print(revers_n)


digits_list = []
for digit in n:
    digits_list.append(digit)

sorted(digits_list)
print(digits_list)
