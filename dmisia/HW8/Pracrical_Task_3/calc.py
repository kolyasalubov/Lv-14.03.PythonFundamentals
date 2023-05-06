import math


def rectangle():
    a = float(input("Enter first value: "))
    b = float(input("Enter second value: "))
    area = a * b
    return f"The are of rectangle: {area}"


def triangle():
    h = float(input("Enter height value: "))
    s = float(input("Enter base value: "))
    area = 0.5 * h * s
    return f"The are of triangle: {area}"


def circle():
    r = float(input("Enter radius value: "))
    area = math.pi * pow(r, 2)
    return f"The are of circle: {area}"