number = int(input("Enter your number: "))

one_div = number//1000
two_div = number % 1000//100
three_div = number % 100//10
four_div = number % 10

# Item 1: find of product of the digits of this number:
prod_of_dig = one_div*two_div*three_div*four_div
print("Product of the digits of this number: ", prod_of_dig)


# Item 2: write the number in reverse order:
str_number = ''.join(reversed(list(str(number))))
print("Reverse of our number: ", str_number)


# Item 3: in ascending order, you need to
# sort the number included in the given number:
sort_number = ''.join(sorted(str(number)))
print("", sort_number)
