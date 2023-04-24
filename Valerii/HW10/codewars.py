# Regular Ball Super Ball

class Ball():
    def __init__(self, ball_type='regular'):
        self.ball_type = ball_type

# Color Ghost

from random import choice as choice

class Ghost():
    colors = ["white", "yellow", "purple", "red"]
    def __init__(self):
        self.color = choice(Ghost.colors)

# Basic subclasses - Adam and Eve

class Human():
    def __init__(self, name):
        self.name = name

class Man(Human):
    pass

class Woman(Human):
    pass


def God():
    adam = Man('Adam')
    eve = Woman('Eve')
    return adam, eve

# Classy Classes

class Person():
    def __init__(self, name, age):
        self.info = f"{name}s age is {age}"
        self.name = name
        self.age = age

# Building Spheres
from math import pi as PI

class Sphere():
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
    def get_radius(self):
        return self.radius
    def get_mass(self):
        return self.mass
    def get_volume(self):
        return round(self.radius**3*PI*4/3, 5)
    def get_surface_area(self):
        return round(4*PI*self.radius**2 , 5)
    def get_density(self):
        volume = self.radius**3*PI*4/3
        return round(self.mass/volume, 5)
    
# Python's Dynamic Classes #1

def class_name_changer(cls, new_name):
    if new_name[0].isupper() and new_name.isalnum():
        cls.__name__ = new_name
    else:
        raise Exception
    
