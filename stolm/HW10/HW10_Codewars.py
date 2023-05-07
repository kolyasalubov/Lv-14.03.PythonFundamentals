# Practical Task


# I. Ball super ball:
# class Ball(object):
#     def __init__(self, ball_type = "regular"):
#         self.ball_type = ball_type


# II. Color ghost:
# import random
# class Ghost(object):
#     def __init__(self):
#         self.color = random.choice(["white", "yellow", "purple", "red"])


# III. Basic subclasses-Adam and Eve:
# def God():
#     return Man(), Woman()

# class Human:
#     pass

# class Man(Human):
#     def __repr__(self):
#         return "First object are a man"

# class Woman(Human):
#     def __repr__(self):
#         return "Second object are a woman"


# IV. Classy classes:
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = int(age)
    
#     @property
#     def info(self):
#         return f"{self.name}s age is {self.age}"


# V. Building Spheres:
# import math
# class Sphere(object):
#     def __init__(self, radius, mass):
#         self.radius = radius
#         self.mass = mass
    
#     def get_mass(self):
#         return self.mass
    
#     def get_radius(self):
#         return self.radius
    
#     def get_volume(self):
#         return round(4/3*math.pi*self.radius**3, 5)
    
#     def get_surface_area(self):
#         return round(4*math.pi*self.radius**2, 5)
    
#     def get_density(self):
#         volume = self.get_volume()
#         return round(self.mass / volume, 5)


# VI. Dynamic Classes:
# def class_name_changer(cls, new_name):
#     if new_name.isalnum() and not new_name[0].islower() and not new_name[0].isdigit():
#         cls.__name__ = new_name
#     else:
#         raise ValueError("Invalid class name.")
