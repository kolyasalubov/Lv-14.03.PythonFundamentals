import calc
figure = int(input("""Enter number of the figure you want to calculate:
1. Rectangle
2. Triangle
3. Circle
"""))

if figure == 1:
    print(calc.rectangle())
elif figure == 2:
    print(calc.triangle())
elif figure == 3:
    print(calc.circle())
else:
    print("No such figure")