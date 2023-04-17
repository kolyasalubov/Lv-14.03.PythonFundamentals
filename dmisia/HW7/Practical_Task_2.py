figure = int(input("""Enter number of the figure you want to calculate:
1. Rectangle
2. Triangle
3. Circle
"""))

def rectangle(a, b):
    return a * b

def triangle(h, s):
    return 0.5 * h * s

def circle(r, PI):
    return PI * r ** 2
    pass


if figure == 1:
    a = int(input("Enter first value: "))
    b = int(input("Enter second value: "))
    print("Your area of rectangle: ", rectangle(a, b))
elif figure == 2:
    h = int(input("Enter height value: "))
    s = int(input("Enter base value: "))
    print("Your area of triangle: ", triangle(h, s))
elif figure == 3:
    r = int(input("Enter radius value: "))
    PI = 3.14
    print("Your area of circle: ", circle(r, PI))
else:
    print("No such figure")