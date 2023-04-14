number = "1234" # Повторить!

reversed_number = 0

mnojenia = 1

for digit in number:
    if digit.isdigit():
        mnojenia *= int(digit)
        
digits = [int(d) for d in str(number)]
sorted_digits = sorted(digits)

sorted_number = ''.join(str(d) for d in sorted_digits)

print("Добуток цифр числа", number, "дорівнює", mnojenia)

print(number[::-1])

print("Цифри в порядку зростання: ", sorted_number)

