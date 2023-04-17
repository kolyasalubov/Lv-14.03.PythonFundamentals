number = int(input('Enter your number to know factorial: '))

if number == 0 or number == 1:
    print(f'{number}! = 1')
elif number < 0:
    print('Try again with positive integer number.')
else:
    factorial = 1
    for n in range(1, number+1):
        factorial *= n
    print(f'{number}! = {factorial}')
