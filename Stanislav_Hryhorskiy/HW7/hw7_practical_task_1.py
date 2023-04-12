# *** Practical task 1 ***
# Write a function that returns the largest number of two numbers
# (use DocStrings documentation strings in the function).

def largest_number(number_1: float, number_2: float) -> str:
    """
    Function that returns the largest number of two numbers
    :param number_1: float
    :param number_2: float
    :return: a message about which of the numbers is larger
    """
    if number_1 > number_2:
        return f"First number is greater than second number: {number_1} > {number_2}."
    elif number_1 < number_2:
        return f"Second number is greater than first number: {number_1} < {number_2}."
    else:
        return f"First and second number is equal: {number_1} = {number_2}."


if __name__ == "__main__":
    num_1 = float(input("Enter the first number: "))
    num_2 = float(input("Enter the second number: "))
    print(largest_number(num_1, num_2))
