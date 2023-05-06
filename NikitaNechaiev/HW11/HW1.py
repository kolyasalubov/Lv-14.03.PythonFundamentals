try:
    '''
    This is program to calculate the divide of two numbers entered by the user
    '''
    numbers = (input('Enter a two numbers through a comma: '))
    num1,num2 = numbers.split(',')
    num1 = int(num1)
    num2 = int(num2) 
    if num1 == 0 or num2 == 0:
        raise ZeroDivisionError('Error!\nZero can`t be divided!.')
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print('Value error!  %s'%e)
else:
    print('The result of deviding is {}'.format(num1/num2))
finally:
    print('Closed!')

#Чи можно в одній программі використовувати  {}.format i %s?