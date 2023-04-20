def larger_number(first, second):
    """
    Function returns the largest number of two numbers.
    Args:
        first: int
        second: int
    returns: int
    """
    return first if first > second else second


print(larger_number(2, 6))