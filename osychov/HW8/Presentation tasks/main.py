import Functions

a = float(input("First number: "))
b = float(input("Second number: "))
def main(a, b):
    choise = int(input("What action you want to do: \n1)Addition \n2)Substraction \n3)Multiplication \n4)Division \n"))
    if choise in range(0, 5):
        if choise == 1:
            print(Functions.addition(a, b))
        elif choise == 2:
            print(Functions.substraction(a, b))
        elif choise == 3:
            print(Functions.multiplication(a, b))
        elif choise == 4:
            print(Functions.division(a, b))
    else:
        print("Enter number from 1 to 4: ")
        main(a, b)
main(a, b)



def main2(): 
    a = float(input("First number: ")) 
    b = float(input("Second number: ")) 
    choice = int(input("What action you want to do: \n1) Addition \n2) Subtraction \n3) Multiplication \n4) Division \n"))

    # Use dictionary to map user's choice to function
    options = {
        1: Functions.addition,
        2: Functions.substraction,
        3: Functions.multiplication,
        4: Functions.division
    }

    if choice in range(1, 5):
        print(options[choice](a, b))
    else:
        print("Enter a number from 1 to 4.")
        main2()

