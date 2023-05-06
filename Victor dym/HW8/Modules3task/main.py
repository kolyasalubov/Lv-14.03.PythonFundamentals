from module_area import *
choose_the_figure = input("Enter your figure: ").lower()

if choose_the_figure == "rectangle":
    rectangle()
elif choose_the_figure == "triangle":
    triangle()
elif choose_the_figure == "circle":
    circle()
else:
    print("error")