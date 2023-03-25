number = 1443
number_string = str(number)
product_of_digits = 1
for i in number_string:
    product_of_digits *= int(i)
print(product_of_digits)
number_reversed = number_string[::-1]
print(number_reversed)
number_sorted = sorted(str(number))
print(number_sorted)