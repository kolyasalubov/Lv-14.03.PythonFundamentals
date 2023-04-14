# *** Practical task 3 ***
# Write a program that calculates the area of a rectangle S=a*b,
# the area of a triangle S=0.5*h*a, the area of a circle S=pi*r**2.
# This module must be used in another module in which we ask the user
# the area of which figure he wants to calculate.
# (To perform the task, you need to import the math module, and from
# it the pow() function and the value of the variable pi, and module,
# which contains three functions for finding areas, into the main program.
# The basic logic of the program is executed in the main module).

from function_module import *


def text_menu():
    """
    Text menu for selecting a geometric shape
    """
    print("Select the figure whose area needs to be calculated:\n"
          "\t1 - rectangle;\n\t2 - triangle;\n\t3 - circle.")


def menu(number: int) -> str:
    """
    The function returns the calculated area of the figure selected by the user
    :param number: int, ordinal number of a geometric figure
    """
    match number:
        case 1:
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            return get_area_rectangle(length, width)
        case 2:
            side = float(input("Enter the side of the triangle: "))
            height = float(input("Enter the height drawn to the entered side: "))
            return get_area_triangle(side, height)
        case 3:
            radius = float(input("Enter the radius of the circle: "))
            return get_area_circle(radius)
        case _:
            return "The menu item was selected incorrectly!"


if __name__ == "__main__":
    text_menu()
    number = int(input("Enter the number of the figure: "))
    print(menu(number))
