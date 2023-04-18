#1 Ball super ball
# Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.
#If no arguments are given, ball objects should instantiate with a "ball type" of "regular."
# class Ball(object):
#     def __init__(self, ball_type = "regular") -> None:
#         self.ball_type = ball_type
        
    
# ball1 = Ball()
# ball2 = Ball("super")   
# print(ball1.ball_type)

#2Color Ghost
# import random

# class Ghost(object):
#   def __init__(self):
#     self.color = random.choice(["white", "yellow", "purple", "red"])
   

# print(Ghost)

#3
# def God():
#     return [man,woman]

# class Human:
#     pass

# class Man(Human):
#     pass

# class Woman(Human):
#     pass

# man = Man()
# woman = Woman()

#4 Classy Classes
# class Person:
#     def __init__(self, name,age):
#         self.info = "{}s age is {}".format(name, age)

#5 Building spheres
# import math
# class Sphere():
#     def __init__(self, radius, mass) :
#         self.radius = radius
#         self.mass = mass
    
#     def get_radius(self):
#         return self.radius
    
#     def get_mass(self):
#         return self.mass
    
#     def get_volume(self):
#         self.volume = 4/3 * math.pi * (self.radius ** 3)
#         return round(self.volume, 5)
    
#     def get_surface_area(self):
#         surface_area = 4 * math.pi * (self.radius**2)
#         return round(surface_area, 5)
    
#     def get_density(self):
#         return round(self.mass / self.volume, 5)
# sph1 = Sphere(5, 10)
# print(sph1.get_volume())
# print(sph1.get_density())


# from math import pi
# class Sphere(object):
#     def __init__(self, radius, mass):
#         self.radius = radius
#         self.mass = mass
#         self.volume = 4*pi * self.radius**3 / 3
#         self.surface = 4*pi* self.radius**2
#     def get_radius(self):
#         return self.radius
#     def get_mass(self):
#         return self.mass
#     def get_volume(self):
#         return round(self.volume,5)
#     def get_surface_area(self):
#         return round(self.surface,5)
#     def get_density(self):
#         return round(self.mass/self.volume, 5)



#6 Dynamic classes (Changing name of class)
digits = "0, 1, 2, 3, 4, 5, 6, 7, 8, 9"
import re
import string
class MyClass:
    pass
obj = MyClass
def class_name_changer(cls, new_name):
    assert new_name[0].isupper() and new_name.isalnum()
    cls.__name__ = new_name
        
class_name_changer(MyClass, "Asasas2")
print(obj.__name__)
#.isalnum() - The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).