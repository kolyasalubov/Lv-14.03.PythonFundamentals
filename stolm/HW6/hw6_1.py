list = [ i for i in range(11) ]
even_two = []
odd_three = []
not_div_two_three = []
index = 0

while list:
    for i in list:
        if i % 2 == 0:
            even_two.append(list.pop(index))
        elif i % 3 == 0:
            odd_three.append(list.pop(index))
        else:
            not_div_two_three.append(list.pop(index))
        index += 1
    index = 0


print(list)
print(even_two)
print(odd_three)
print(not_div_two_three)
