import math

def rectangle_area():
    length = float(input("Enter the length of rectangle: "))
    width = float(input("Enter the width of rectangle: "))
    return f"The area of rectangle is {length * width}"

def triangle_area():
    base = float(input("Enter the length of base of triangle: "))
    height = float(input("Enter the length of height of triangle: "))
    return f"The area of triangle is {1/2 * base * height}"

def circle_area():
    radius = float(input("Enter the length of radius of circle: "))
    return f"The area of circle is {(math.pi * math.pow(radius, 2)).__round__(2)}"
