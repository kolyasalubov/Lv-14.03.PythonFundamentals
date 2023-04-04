string = "1256"
number = list(string)
print(f"Product of the digits of this number - {int(number[0]) * int(number[1]) * int(number[2]) * int(number[3])}")
print(string[::-1])
sort_number = ''.join(sorted(string))
print("Ascending order of digits in the number:", sort_number)



# number = int(input("Enter your number: "))

# one_div, remainder = divmod(number, 1000)
# two_div, remainder = divmod(remainder, 100)
# three_div, four_div = divmod(remainder, 10)

# #Item 1: find of product of the digits of this number:
# prod_of_dig = one_div * two_div * three_div * four_div
# print("Product of the digits of this number:", prod_of_dig)

# #Item 2: write the number in reverse order:
# str_number = str(number)[::-1]
# print("Reverse of our number:", str_number)

# #Item 3: in ascending order, you need to sort the number included in the given number:
# sort_number = ''.join(sorted(str(number)))
# print("Ascending order of digits in the number:", sort_number)
