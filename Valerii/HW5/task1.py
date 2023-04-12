l = [int(input('Enter integer number: ')) for number in range(int(input('Enter numbers quantity: ')))]
for number in range(len(l)):
    l[number] = float(l[number])
print('Your list of float numbers: ', l)
