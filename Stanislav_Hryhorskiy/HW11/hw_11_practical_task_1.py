# *** Task 1 ***
# Write a program that prompts the user to enter
# their age, and then displays a message stating
# whether the age is even or odd. The program must
# provide the ability to enter a negative number,
# and in this case generate an exception.
# The master code should call a function
# that processes the information entered.

def is_even_odd(number: int) -> str:
    """
    Function that return text 'even' or 'odd' is entered number
    """
    if number % 2:
        return "odd"
    return "even"


def is_negative_number(number: int) -> None:
    """
    Function that raise 'ValueError' if argument is a negative number
    """
    if number < 0:
        raise ValueError("a person's age can't be a negative number!")


def main(literal: str) -> None:
    """
    Function that return information about age of user (odd or even).
    In case of incorrect data, an exception 'ValueError' is raised.
    """
    try:
        is_negative_number(int(literal))
    except ValueError as error:
        print(f"ValueError: {error}")
    else:
        print(f"Entered age is {is_even_odd(int(literal))}.")


if __name__ == "__main__":
    main(input("Enter your age: "))
