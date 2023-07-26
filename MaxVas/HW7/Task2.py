rect_area = lambda a, b: a * b
triang_area = lambda a, b: 0.5 * a * b
circ_area = lambda a: a * 3.14

def main():
    print("Enter 1 for rectangle;", "Enter 2 for triangle;", "Enter 3 for circle;", sep="\n")
    enter = int(input(""))
    if enter == 1:
        print(rect_area(float(input("Enter rectangle length: ")), float(input("Enter the width of width: "))))
    elif enter == 2:
        print(triang_area(float(input("Enter triangle's base length: ")), float(input("Enter the length of Height perpendicular to base: "))))
    elif enter == 3:
        print(circ_area(float(input("Enter circle radius: "))))
    else:
        print("Number out of list!")
main()