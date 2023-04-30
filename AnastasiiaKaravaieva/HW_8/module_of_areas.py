import math


def triangle_area(h, a):
    s = 0.5 * h * a
    return int(s)


def rectangle_area(a, b):
    s = a * b
    return s


def circle_area(r):
    s = pow(r, 2)*math.pi
    return round(s, 2)