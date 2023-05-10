# *** Task 5 ***
# Find the largest item in the list using the reduce function

from functools import reduce


def max_two_vars(var_one, var_two):
    if var_one > var_two:
        return var_one
    return var_two


def max_len_two_vars(var_one, var_two):
    if len(var_one) > len(var_two):
        return var_one
    return var_two


num_list = [57, -23, 30, 102, 0]
max_item = reduce(lambda x, y: x if (x > y) else y, num_list)
print(max_item)

num_list = [57, -23, 30, 102, 0]
max_item = reduce(max_two_vars, num_list)
print(max_item)

str_list = ["python", "language", "code", "zen", "decorator"]
largest_item = reduce(lambda x, y: x if (len(x) > len(y)) else y, str_list)
print(largest_item)

str_list = ["python", "language", "code", "zen", "decorator"]
largest_item = reduce(max_len_two_vars, str_list)
print(largest_item)
