import functions

def main():
    print("Which area you want to calculate: ")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    def choice():
        inp = int(input("Enter your choice from 1 to 3: "))
        if inp == 1:
            print(functions.rectangle_area())
        elif inp == 2:
            print(functions.triangle_area())
        elif inp == 3:
            print(functions.circle_area())
        else:
            print("Please, Enter number from 1 to 3! ")
            choice()
    choice()
main()
        