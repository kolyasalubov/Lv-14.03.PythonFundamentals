def area_rectangle(length: int, width: int) -> int:
    return length * width


def area_triangle(height: int, base: int) -> float:
    return (base * height) / 2


def area_circle(radius: int) -> float:
    return PI * (radius ** 2)


PI = 3.14
finding = input("What kind of figure do you need the area for?:")
while finding != "rectangle" or "triangle" or "circle":
    another_try = input(f"Your figure printed incorrect. Please, try again instead of({finding}):")
    finding = another_try
    if finding.lower() == "rectangle":
        rectangle = area_rectangle(length=int(input("Enter length of your Rectangle:")),
                                   width=int(input("Enter width of your Rectangle:")))
        print("The Area of Rectangle is:", rectangle)
        break
    elif finding.lower() == "triangle":
        triangle = area_triangle(height=int(input("Enter height of your Triangle:")),
                                 base=int(input("Enter base of your Triangle:")))
        print("The Area of Triangle is:", triangle)
        break
    elif finding.lower() == "circle":
        circle = area_circle(radius=int(input("Enter radius of your Circle:")))
        print("The Area of your Circle is:", circle)
        break
