"""
*** Practical task 2 ***
A four-digit natural number is specified:
- find the product of the digits of this number;
- write the number in reverse order;
- in ascending order, you need to sort the numbers included in the given number.
"""

number = int(input('Enter a four-digit integer: '))

print()
num_list = list(str(number))
product = int(num_list[0]) * int(num_list[1]) * int(num_list[2]) * int(num_list[3])
print(f"Product the digits of number {number} is equal: {product}")
print(f"Number {number} wrote in reverse order: {str(number)[::-1]}")
num_list.sort()
print(f"Sorted in ascending order the numbers included number {number}:", *num_list)

print()
d = number % 10
number_1 = (number - d) // 10
c = number_1 % 10
number_2 = (number_1 - c) // 10
b = number_2 % 10
number_3 = (number_2 - b) // 10
a = number_3 % 10
product = a * b * c * d
print(f"Product the digits of number {number} is equal: {product}")
print(f"Number {number} wrote in reverse order: {d}{c}{b}{a}")
new_list = [a, b, c, d]
new_list.sort()
print(f"Sorted in ascending order the numbers included number {number}:", *new_list)
