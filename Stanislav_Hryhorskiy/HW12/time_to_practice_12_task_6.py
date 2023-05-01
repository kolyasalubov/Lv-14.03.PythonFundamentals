# *** Task 6 ***
# Create a simple generator function similar to the range iterator

def prime_numbers(number):
    """
    Function that return generator object with first 'number' prime numbers
    :param number: int
    """
    count, value = 1, 2
    while count <= number:
        for divider in range(2, value):
            if not value % divider:
                break
        else:
            yield value
            count += 1
        value += 1


number_of_primes = 25
result = prime_numbers(number_of_primes)
print(f'The list of first {number_of_primes} prime numbers:\n{list(result)}')
