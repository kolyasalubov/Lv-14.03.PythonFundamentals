# Write a function that returns
# the arithmetic mean of any number of numbers.

def mean(*numbers: float) -> str:
    """
    Function that returns the arithmetic mean
    of any number of numbers
    :param numbers: float
    :return: arithmetic mean of real numbers
    """
    result = None
    if len(numbers):
        result = sum(numbers) / len(numbers)
    return f"Arithmetic mean of input numbers is: {result:.2f}"


if __name__ == "__main__":
    print(mean(0, 1, 1, 2, 3, 5, 8, 13, 21, 34))
