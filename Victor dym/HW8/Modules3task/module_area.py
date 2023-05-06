import math
from math import pow
from math import pi

def rectangle():
    a = int(input("Enter the a side"))
    b = int(input("Enter the b side"))
    print(a * b)

def triangle():
    h = int(input("Enter the height"))
    a = int(input("Enter the a side"))
    print(0.5 * h * a)

def circle():
    r = int(input("Enter the radius"))
    print(pi * r**2)

