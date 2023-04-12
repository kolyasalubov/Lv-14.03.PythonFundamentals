from math import pi


def area_rectangle(a, b):
    """ This function calculates the area of recnangle with sides:
    a, b
    """
    return a*b

def area_triangle(a, h):
    """ This function calculates the area of triangle 
    with side 'a' and hight 'h' to it.
    """
    return a*h/2

def area_circle(r):
    """ This function calculates the area of circle with radius 'r'."""
    return pi*r**2

def calculate_throuht_input():
    """ The main function, that calculates the area of rectangle, triangle or circle
    depending on the user's choise.    
    """
    choise = input('Hello, what area do you want to calculate?\nEnter rectange/triangle/circle: ')
    if choise == 'rectangle':
        a = int(input('a = '))
        b = int(input('b = '))
        print('The area is ', area_rectangle(a, b))
    elif choise == 'triangle':
        a = int(input('a = '))
        h = int(input('h = '))
        print('The area is ', area_triangle(a, h))
    elif choise == 'circle':
        r = int(input('r = '))
        print('The area is ', round(area_circle(r), 2))
    else:
        print('Incorrect input, try again :(')

