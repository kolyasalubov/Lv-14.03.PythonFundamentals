try:
    elements = int(input('''Please, tell how many elements
    from Fibonacci`s sequence you`d like to see: '''))  
    fibonacci_numbers = [0, 1]
    if elements == 0 or elements == 1:
        print(0) 
    else:  
        for i in range(2, elements):
            fibonacci_numbers.append(fibonacci_numbers[i-2]+fibonacci_numbers[i-1])
        print(fibonacci_numbers)   
except:
    print('Are you okay?')
    