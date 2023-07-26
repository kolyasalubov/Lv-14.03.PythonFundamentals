import math

def rectangle_area(length, width):
    
    return length * width

def triangle_area(base, height):
   
    return 0.5 * base * height

def circle_area(radius):
    
    return math.pi * radius ** 2

print("Make your choice:")
print("Rectangle")
print("Triangle")
print("Circle")

choice = input("Make your choice:")

if choice == "Rectangle":
    length = float(input("Length of the rectangle: "))
    width = float(input("Width of the rectangle: "))
    area = rectangle_area(length, width)
    print(f"The area of the rectangle is {area:.2f}")
elif choice == "Triangle":
    base = float(input("Base of the triangle: "))
    height = float(input("Height of the triangle: "))
    area = triangle_area(base, height)
    print(f"The area of the triangle is {area:.2f}")
elif choice == "Circle":
    radius = float(input("Radius of the circle: "))
    area = circle_area(radius)
    print(f"The area of the circle is {area:.2f}")
else:
    print("Error - please enter valid choice")
