fib_len = int(input('Enter Fibonacci list lenght: '))

l = [0, 1]

if fib_len == 1:
    print('Fibbonacci list: ', l[0])
elif fib_len == 2:
    print('Fibbonacci list: ', l[0], l[1])
elif fib_len <= 0:
    print('Try again with positive integer number.')
else:
    for number in range(2, fib_len):
        new_number = l[number-1] + l[number-2]
        l.append(new_number)
    print('Fibbonacci list: ', l)
