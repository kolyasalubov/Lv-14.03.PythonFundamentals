from math import pi
from math import pow


def rectangle(width, length):
    """
    function to calculate the rectangle, we need two parameters
    length and width of the rectangle
    """
    return width * length


def triangle(height, hypotenuse):
    """
    function to calculate a triangle, we need two parameters height and hypotenuse.
    our function will return the result of the area of the triangle
    """
    return (height*hypotenuse)/2


def circle(r):
    """
    function to calculate the area of a circle, we need one parameter - the radius of
    the circle our function will return the result of the area of the triangle
    """

    return pi * pow(r, 2)
