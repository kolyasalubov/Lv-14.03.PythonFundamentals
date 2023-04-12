import math


def triangle_area(h, a):
    s = 1 / 2 * h * a
    return int(s)


def rectangle_area(a, b):
    s = a * b
    return s


def circle_area(r):
    s = r**2*math.pi
    return round(s, 2)


area = input("What kind of area do you want to find?")

if area == "triangle":
    h_t = int(input("Write the height of triangle:"))
    a_t = int(input("Write the side of triangle:"))
    print(triangle_area(h_t, a_t))
elif area == "rectangle":
    a_r = int(input("Write the first side of rectangle:"))
    b_r = int(input("Write the second side of rectangle:"))
    print(rectangle_area(a_r, b_r))
elif area == "circle":
    r_c = int(input("Write the r of the circle:"))
    print(circle_area(r_c))
else:
    print("I don't know how to find the area of this figure")