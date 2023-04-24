import functions

def main():
    print("Enter 1 for rectangle;", "Enter 2 for triangle;", "Enter 3 for circle;", sep="\n")
    enter = int(input(""))
    if enter == 1:
        print(functions.rect_area(float(input("Enter rectangle length: ")), float(input("Enter the width of width: "))))
    elif enter == 2:
        print(functions.triang_area(float(input("Enter triangle's base length: ")), float(input("Enter the length of Height perpendicular to base: "))))
    elif enter == 3:
        print(functions.circ_area(float(input("Enter circle radius: "))))
    else:
        print("Number out of list!")

main()