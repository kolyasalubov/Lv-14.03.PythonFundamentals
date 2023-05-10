num =  (input('Enter a number: '))
try:
    num = int(num)
    if num == 1:
        print('Monday')
    elif num == 2:
        print('Tuesday')
    elif num == 3:
        print('Wednesday')
    elif num == 4:
        print('Thursay')
    elif num == 5:
        print('Friday')
    elif num == 6:
        print('Saturday')
    elif num == 7:
        print('Sunday')
    elif num >= 8:
        print('You can input only from 1 to 7.')
    else:
        print('Value Error')
except ValueError as e:
    print('Wrong number %s'%e)