from math import pi, pow


def get_area_rectangle(a: float, b: float) -> str:
    """
    Function that calculate the area of the rectangle
    :param a: float
    :param b: float
    :return: result with information of the area of the rectangle
    """
    area = a * b
    return f"The area of the rectangle with the sides a = {a}, b = {b} " \
           f"is equal: S = {area:.2f}"


def get_area_triangle(a: float, h: float) -> str:
    """
    Function that calculate the area of the triangle
    :param a: float, side of the triangle
    :param h: float, the height drawn to the given side of the triangle
    :return: result with information of the area of the triangle
    """
    area = 0.5 * a * h
    return f"The area of the triangle with a side a = {a}, and height h = {h} " \
           f"is equal: S = {area:.2f}"


def get_area_circle(r: float) -> str:
    """
    Function that calculate the area of the circle
    :param r: float, radius of the circle
    :return: result with information of the area of the circle
    """
    area = pi * pow(r, 2)
    return f"The area of the triangle with a radius r = {r} " \
           f"is equal: S = {area:.2f}"
