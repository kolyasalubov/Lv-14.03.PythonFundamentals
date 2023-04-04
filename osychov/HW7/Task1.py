def what_number_is_larger(a,b):
    """_In this function we determine which input two numbers is larger_

    Args:
        a (_int_): _first number_
        b (_int_): _second number_
    """
    
    if a > b:
        return f"{a} is greater than {b}"
    elif a < b:
        return f"{b} is greater than {a}"
    else:
        return f"{a} and {b} are equal"
print(what_number_is_larger.__doc__)
print(what_number_is_larger(4, 5))