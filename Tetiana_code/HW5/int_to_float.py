orig_list = [1, 2, 3, 4, 5, 6, 7, 8]
new_list = list()
for x in orig_list:
    new_list.append(float(x))

orig_list = new_list
print(orig_list)