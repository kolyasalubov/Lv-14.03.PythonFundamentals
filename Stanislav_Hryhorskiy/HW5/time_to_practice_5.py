"""
Print all even numbers less than 100 (write two variants of the code:
one using the while loop, and the other using the for loop).
"""

number = 0
while number < 100:
    if not number % 2:
        print(number, end=', ')
    number += 1
print()

for number in range(0, 100, 2):
    print(number, end=', ')
print()

for number in range(0, 100):
    if not number % 2:
        print(number, end=', ')
print()

"""
Print all odd numbers less than 100. (write two versions of the code:
one using the continue operator, and the other without this operator).
"""

for number in range(1, 100, 2):
    print(number, end=', ')
print()

for number in range(0, 100):
    if not number % 2:
        continue
    print(number, end=', ')
print()

"""
Check if the list contains odd numbers.
(Hint: use the break statement)
"""

new_list = [6, 8, 12, 15, 17, 0, 25, 14]
for item in new_list:
    if item % 2:
        print(f"This list contains odd numbers")
        break