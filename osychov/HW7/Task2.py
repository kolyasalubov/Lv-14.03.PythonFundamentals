import math

def rectangle_area():
    a = float(input("Write the length of rectangle: "))
    b = float(input("Write the width of width: "))
    area = a * b
    return f"Area of rectangle = {area}"

def triangle_area():
    base = float(input("Write the length of base of triangle: "))
    height = float(input("Write the length of Height perpendicular to base: "))
    area  = 1/2 (base * height)
    return f"Area of triangle = {area}"

def circle_area():
    radius = float(input("Write a radius of the circle: "))
    area = math.pi * radius
    return f"The area of the circle is {area}"

def main():
    print("Which area you want to calculate: ")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    inp = int(input("Enter your choice from 1 to 3: "))
    if inp == 1:
        print(rectangle_area())
    elif inp == 2:
        print(triangle_area())
    elif inp == 3:
        print(circle_area())
    else:
        print("Please, Enter number from 1 to 3! ")
        
main()
        

    
    