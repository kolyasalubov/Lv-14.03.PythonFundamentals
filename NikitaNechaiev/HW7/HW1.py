def largest_number(num1,num2):
    '''

     DocString 
    
     That functions
     returns the 
     largest number 
     of two numbers
    '''
    if num1 > num2:
        return f'Number {num1} -> is larger than {num2}.' 
    elif num1 < num2:
        return f'Number {num2} -> is larger than {num1}.'
    
     
print(largest_number(100,63))
print(largest_number(-2,1))
print(largest_number(-32,-56))
print(largest_number.__doc__)