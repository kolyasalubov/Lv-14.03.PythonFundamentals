
import math

def rectangle_area(a, b):
    return a * b

def triangle_area(h, a):
    return 0.5 * h * a

def circle_area(r):
    return math.pi * math.pow(r, 2)

def main():
    print("Choose a figure")
    print("Rectangle")
    print("Triangle")
    print("Circle")
    
    choice = str(input("Enter your choice: "))
    
    if choice == 1:
        a = float(input("Length of the rectangle: "))
        b = float(input("Width of the rectangle: "))
        print("Rectangle area: ", rectangle_area(a, b))
    elif choice == 2:
        h = float(input("Height of the triangle: "))
        a = float(input("Base of the triangle: "))
        print("Triangle area: ", triangle_area(h, a))
    elif choice == 3:
        r = float(input("Radius of the circle: "))
        print("Circle area: ", circle_area(r))
    else:
        print("Please enter valid choice.")

if __name__ == '__main__':
    main()

