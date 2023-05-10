# QUESTION 1
# Create a decorator that adds a "tag" to a string.
# The tag will be specified as an argument to the decorator.

def add_tag(tag):
    def decorator(func):
        def inner():
            return f"{tag}{func()}{tag}"

        return inner

    return decorator


# QUESTION 2
# Write a list comprehension function celsius_to_fahrenheit(temps)
# whose input parameter is a list of temperatures in Celsius.
# The function returns new array where temps in Farenheit.
# Hint: F = (C * 9/5) + 32.

def celsius_to_fahrenheit(temps):
    return [9 * item / 5 + 32 for item in temps]


# QUESTION 3
# Write fibonacci_numbers function which returns
# a generator that yields the Fibonacci sequence.

def fibonacci_numbers():
    num_prev, num_next = 0, 1
    while True:
        yield num_prev
        num_prev, num_next = num_next, num_prev + num_next


fib = fibonacci_numbers()


# QUESTION 4
# Write a generator function that returns
# all combinations of two lists.

def combinations(list1, list2):
    for item_1 in list1:
        for item_2 in list2:
            yield item_1, item_2


# QUESTION 5
# Write a function celsius_to_fahrenheit(temps) using map function
# whose input parameter is a list of temperatures in Celsius.
# The function returns new array where temps in Farenheit.
# Hint: F = (C * 9/5) + 32

def celsius_to_fahrenheit(temps):
    return list(map(lambda x: 9 * x / 5 + 32, temps))
