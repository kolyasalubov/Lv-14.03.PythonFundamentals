# *** Task 3 ***
# All these numbers in the list have a string data type,
# for example ['1', '2', '3', '4', '5', '7'], convert this
# list to a list, all numbers of which have the data type integer:
# 1) using the append method
# 2) using the map method

str_list = ['1', '2', '3', '4', '5', '7']

# Variant 1 (using the append method)
num_list = []
for item in str_list:
    num_list.append(int(item))
print(num_list)

# Variant 2 (using the map method)
num_list = list(map(int, str_list))
print(num_list)
