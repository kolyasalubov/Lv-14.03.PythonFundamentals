def largest_number(a: int, b: int) ->int:
    """ The function returns the largest number of two.
    a, b: int
    """
    if a > b:
        return a
    elif b > a:
        return b
    else: return 'Numbers are equal'
