"""
*** Practical task 1 ***
Create a list that contains elements of integer type, then use
the loop to change the type of these elements to a floating type.
(Hint: use the built-in float() function).
"""

from random import randint

# Created new int_list with integers
int_list, len_list = [], randint(2, 10)
for item in range(len_list):
    int_list.append(randint(1, 100))
print(f"A list that contains elements of integer type:\n{int_list}")
print()

# Change the type of elements in int_list (created new float_list)
float_list = []
for element in int_list:
    float_list.append(float(element))
print(f"Changed list that contains elements of float type:\n{float_list}")
print()

float_list_new = list(map(float, int_list))
print(f"Changed list that contains elements of float type:\n{float_list_new}")
