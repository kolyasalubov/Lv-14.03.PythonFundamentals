def get_add_num(first_number, second_number: float) -> str:
    """
    Function that return the sum of two numbers
    :param first_number: float
    :param second_number: float
    :return: information about the sum of two numbers
    """
    return f"The addition of two numbers: X + Y = {first_number + second_number}"


def get_sub_num(first_number, second_number: float) -> str:
    """
    Function that return the subtraction of two numbers
    :param first_number: float
    :param second_number: float
    :return: information about the subtraction of two numbers
    """
    return f"The subtraction of two numbers: X - Y = {first_number - second_number}"


def get_mult_num(first_number, second_number: float) -> str:
    """
    Function that return the multiplication of two numbers
    :param first_number: float
    :param second_number: float
    :return: information about the multiplication of two numbers
    """
    return f"The multiplication of two numbers: X * Y = {first_number * second_number}"


def get_div_num(first_number, second_number: float) -> str:
    """
    Function that return the division of two numbers
    :param first_number: float
    :param second_number: float
    :return: information about the division of two numbers
    """
    if second_number:
        return f"The division of two numbers: X / Y = {first_number / second_number}"
    else:
        return "You can't divide by zero!!!"


def get_text_menu():
    """
    A menu for selecting a mathematical operation on two numbers
    """
    print("""Select the number of the math operation: 
    \t1. The addition of two numbers (X + Y);
    \t2. The subtraction of two numbers (X - Y);
    \t3. The multiplication of two numbers (X * Y);
    \t4. The division of two numbers (X / Y).""")


def get_math_operation(operation_number: int,
                       first_number: float,
                       second_number: float) -> None:
    """
    A function for performing one of the mathematical operations
    (addition, subtraction, multiplication, division) on two numbers
    :param operation_number: int
    :param first_number: float
    :param second_number: float
    """
    match operation_number:
        case 1:
            print(get_add_num(first_number, second_number))
        case 2:
            print(get_sub_num(first_number, second_number))
        case 3:
            print(get_mult_num(first_number, second_number))
        case 4:
            print(get_div_num(first_number, second_number))
        case _:
            print("The number of a mathematical operation on two numbers was incorrectly selected!")
