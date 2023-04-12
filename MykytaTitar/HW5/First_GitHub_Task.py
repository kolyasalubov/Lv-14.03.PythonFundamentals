# Making list with floats from lists with integers

integer_list = [5, 2346, 78, 234, 45, 124]

float_list = []

for number in integer_list[:]:
    float_list.append(float(number))


print(float_list)
