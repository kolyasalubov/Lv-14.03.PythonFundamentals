num = int(input('Enter four-digit natural number: '))
search2 = int(input('1) Find the product of the digits of number".\n'
                    '2) Write the number in reverse order.\n'
                    '3) In ascending order, sort the numbers included in the given number"\n'
                    'Enter number of action you need to perform: '))
num1 = (num // 1000)
num2 = (num % 1000 // 100)
num3 = (num % 100 // 10)
num4 = (num % 10)
if search2 == 1:
    print('Your answer is ', num1 * num2 * num3 * num4)
elif search2 == 2:
    print('Your reverse number: ',str(num4) + str(num3) + str(num2) + str(num1))
elif search2 == 3:
    list1 = [int(d) for d in str(num)]
    sort = (sorted(list1))
    num0 = 0
    for i in sort:
        num0 = num0 * 10 + i
    print('Your sorted number: ',num0)
else:
    print('Action is incorrect')