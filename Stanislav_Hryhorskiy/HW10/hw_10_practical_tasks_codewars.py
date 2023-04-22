# I. Ball super ball
# Create a class Ball. Ball objects should accept
# one argument for "ball type" when instantiated.
# If no arguments are given, ball objects should
# instantiate with a "ball type" of "regular."

class Ball:

    def __init__(self, ball_type='regular'):
        self.ball_type = ball_type


# II. Color ghost
# Create a class Ghost
# Ghost objects are instantiated without any arguments.
# Ghost objects are given a random color attribute of "white"
# or "yellow" or "purple" or "red" when instantiated
from random import choice


class Ghost:
    color_list = ["white", "yellow", "purple", "red"]

    def __init__(self):
        self.color = choice(self.__class__.color_list)


# III. Basic subclasses-Adam and Eve
# According to the creation myths of the Abrahamic religions,
# Adam and Eve were the first Humans to wander the Earth.
# You have to do God's job. The creation method must return
# an array of length 2 containing objects (representing Adam
# and Eve). The first object in the array should be an instance
# of the class Man. The second should be an instance of the class
# Woman. Both objects have to be subclasses of Human. Your job is
# to implement the Human, Man and Woman classes.


def God():
    return Man(), Woman()


class Human:
    pass


class Man(Human):
    def __repr__(self):
        return "First object are a man"


class Woman(Human):
    def __repr__(self):
        return "Second object are a woman"


# IV. Classy classes
# Basic Classes, this kata is mainly aimed
# at the new JS ES6 Update introducing classes
# Your task is to complete this Class, the Person class
# has been created. You must fill in the Constructor method
# to accept a name as string and an age as number, complete
# the get Info property and getInfo method/Info getter which
# should return 'johns age is 34'


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def info(self):
        return f"{self.name}s age is {self.age}"


# V. Building Spheres
# Now that we have a Block let's move on
# to something slightly more complex: a Sphere.
from math import pi


class Sphere:
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        return round(4 * pi / 3 * self.radius ** 3, 5)

    def get_surface_area(self):
        return round(4 * pi * self.radius ** 2, 5)

    def get_density(self):
        return round(3 * self.mass / (4 * pi * self.radius ** 3), 5)


# VI. Dynamic Classes
# Timmy's quiet and calm work has been suddenly stopped
# by his project manager (let's call him boss) yelling:
# - Who named these classes?! Class MyClass? It's ridiculous!
# I want you to change it to UsefulClass!
# Tim sighed, he already knew it's gonna be a long day.
# Few hours later, boss came again:
# Much better - he said - but now I want to change that class
# name to SecondUsefulClass, and went off. Although Timmy had
# no idea why changing name is so important for his boss, he realized,
# that it's not the end, so he turned to you, his guru, to help him and
# asked you to prepare some function, which could change name of given class.
# Note: Proposed function should allow only names with alphanumeric chars
# (upper & lower letters plus ciphers), but starting only with upper case letter.
# In other case it should raise an exception. Disclaimer: there are obviously
# betters way to check class name than in example cases, but let's stick with
# that, that Timmy yet has to learn them.

def class_name_changer(cls, new_name: str):
    if new_name[0].isupper() and new_name.isalnum():
        cls.__name__ = new_name
    else:
        raise NameError("Invalid class name format!")
