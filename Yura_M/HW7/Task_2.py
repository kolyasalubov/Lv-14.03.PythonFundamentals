# Task2. Write a program that calculates the area of a rectangle,
# triangle and circle
# (write three functions to calculate the area, and call them in the
# main program depending on the user's choice).


def rec(width, length):
    """
    function to calculate the rectangle, we need two parameters
    length and width of the rectangle
    """
    return width * length


def tri(height, hypotenuse):
    """
    function to calculate a triangle, we need two parameters height and hypotenuse.
    our function will return the result of the area of the triangle
    """
    return (height*hypotenuse)/2


def circ(r):
    """
    function to calculate the area of a circle, we need one parameter - the radius of
    the circle our function will return the result of the area of the triangle
    """
    PI = 3.14
    return PI * r**2


choise = int(input(
    "to calculate the area of a rectangle, enter - 1, for a triangle enter - 2, for a circle enter - 3 : "))

if choise == 1:
    rectangle = rec(int(input("enter widh: ")), int(input("enter lengh: ")))
    print("the area of the rectangle is equal to: ", rectangle)
if choise == 2:
    triangle = tri(int(input("enter height: ")),
                   int(input("enter hypotenuse: ")))
    print("the area of the triangle is equal to: ", triangle)
if choise == 3:
    circle = circ(int(input("enter radius: ")))
    print("the area of the circle is equal to: ", circle)
