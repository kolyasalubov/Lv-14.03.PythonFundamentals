def area_rectangle(a, b):
    return a*b


def area_triangle(a, h):
    return 0.5*a*h


def area_circle(r):
    return 3.14*pow(r, 2)


def menu():
    choice = int(input("Enter your choice: "))
    if choice == 1:
        a = int(input("Enter the first side of your rectangle: "))
        b = int(input("Enter the other side of your rectangle: "))
        print(
            f"Area of triangle with the first side of {a} cm and the second side of {b} cm: ",
            area_rectangle(a, b))
    elif choice == 2:
        a = int(input("Enter the base of your triangle: "))
        h = int(input("Enter the height of your triangle: "))
        print(
            f"Area of triangle with the base of {a} cm and the height of {h} cm: ",
            area_triangle(a, h))
    elif choice == 3:
        r = int(input("Enrer radius of your circle: "))
        print(
            f"Area of circle with the radius of {r} cm: ",
            area_circle(r))
    else:
        return "The item you selected is not on the menu!"


if __name__ == "__main__":
    print( """  =====\tMENU: =====
        1. Find the area of the rectangle;
        2. Find the area of the triangle;
        3. Find the area of the circle; """)
    menu()
