
import Find_area as ar


choise = int(input(
    "to calculate the area of a rectangle, enter - 1, for a triangle enter - 2, for a circle enter - 3 : "))

if choise == 1:
    rectangle = ar.rectangle(int(input("enter widh: ")),
                             int(input("enter lengh: ")))
    print("the area of the rectangle is equal to: ", rectangle)
if choise == 2:
    triangle = ar.triangle(int(input("enter height: ")),
                           int(input("enter hypotenuse: ")))
    print("the area of the triangle is equal to: ", triangle)
if choise == 3:
    circle = ar.circle(int(input("enter radius: ")))
    print("the area of the circle is equal to: ", circle)
