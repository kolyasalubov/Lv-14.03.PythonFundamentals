# number = 1443
# number_string = str(number)
# product_of_digits = 1
# for i in number_string:
#     product_of_digits *= int(i)
# print(product_of_digits)
# number_reversed = number_string[::-1]
# print(number_reversed)
# number_sorted = sorted(str(number))
# print(number_sorted)

#Second version:

number = int(input("Enter your number: "))

one_div, remainder = divmod(number, 1000)
two_div, remainder = divmod(remainder, 100)
three_div, four_div = divmod(remainder, 10)

# Item 1: find of product of the digits of this number:
prod_of_dig = one_div * two_div * three_div * four_div
print("Product of the digits of this number:", prod_of_dig)

# Item 2: write the number in reverse order:
str_number = str(number)[::-1]
print("Reverse of our number:", str_number)

# Item 3: in ascending order, you need to sort the number included in the given number:
sort_number = ''.join(sorted(str(number)))
print("Ascending order of digits in the number:", sort_number)