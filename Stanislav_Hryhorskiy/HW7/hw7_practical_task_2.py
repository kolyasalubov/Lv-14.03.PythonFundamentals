# *** Practical task 2 ***
# Write a program that calculates the area of a rectangle,
# triangle and circle (write three functions to calculate the area.
# And call them in the main program depending on the user's choice).
from math import pi


def text_menu():
    """
    A function for displaying a shape selection menu
    """
    print("Select the figure whose area needs to be calculated:\n"
          "\t1 - circle;\n\t2 - rectangle;\n\t3 - triangle.")


def menu(number: int) -> str:
    """
    The function returns the calculated area of the figure selected by the user
    :param number: int
    """
    match number:
        case 1:
            radius = float(input("Enter the radius of the circle: "))
            return get_area_circle(radius)
        case 2:
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            return get_area_rectangle(length, width)
        case 3:
            side_1 = float(input("Enter the first side of the triangle: "))
            side_2 = float(input("Enter the second side of the triangle: "))
            side_3 = float(input("Enter the third side of the triangle: "))
            return get_area_triangle(side_1, side_2, side_3)
        case _:
            return "The menu item was selected incorrectly!"


def get_area_circle(radius: float) -> str:
    """
    Function that calculate area of the circle
    :param radius: float
    :return: message about the result of calculating the area of a circle
    """
    area = pi * radius ** 2
    return f"The area of the circle with a radius {radius} linear units" \
           f" is: S = {area:.2f} square units."


def get_area_rectangle(length: float, width: float) -> str:
    """
    Function that calculate area of the rectangle
    :param length: float
    :param width: float
    :return: message about the result of calculating the area of a rectangle
    """
    area = length * width
    return f"The area of the rectangle with sides {length}, {width} linear units" \
           f" is: S = {area:.2f} square units."


def get_area_triangle(side_1: float, side_2: float, side_3: float) -> str:
    """
    Function that calculate area of the triangle
    :param side_1: float
    :param side_2: float
    :param side_3: float
    :return: message about the result of calculating the area of a triangle
    """
    half_perimeter = 0.5 * (side_1 + side_2 + side_3)
    area = (half_perimeter * (half_perimeter - side_1) * (half_perimeter - side_2) * (half_perimeter - side_3)) ** 0.5
    return f"The area of the triangle with sides {side_1}, {side_2}, {side_3} linear units" \
           f" is: S = {area:.2f} square units."


if __name__ == "__main__":
    text_menu()
    menu_item = int(input("Enter the number of the figure: "))
    print(menu(menu_item))
