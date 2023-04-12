list1 = []
list2 = []
list3 = []

for i in range(1,11):
    if i%2 == 0:
        list1.append(i)
    elif i%3 == 0:
        list2.append(i)    
    else:
        list3.append(i)    

print(f'In range 1 to 10, even numbers that are divisible by 2:\n{list1}')        
print(f'Odd numbers that are divisible by 3:\n{list2}')
print(f'Numbers that are not divisible by 2 and 3:\n{list3}')