################################################# Ball super Ball##############

# class Ball():

#     def __init__(self, ball_type = 'regular') -> None:
#         self.ball_type = ball_type


################################################ Color Ghost ####################
# from random import choice


# class Ghost():

#     def __init__(self) -> None:
#         self.color = choice(["white", "yellow",  "purple", "red"])
#         print(self.color)


# ghosts = [Ghost().color for _ in range(100)]

########################################################## Basic subclasses - Adam and Eve ##########################
# def God():
#     return Man(), Woman()

# class Human():
#     pass

# class Man (Human):
#     def __repr__(self) -> None:
#         return "First object are a man"

# class Woman (Human):
#     def __repr__(self) -> None:
#         return "Second object are a woman"


########################################################## Classy Classes ###########################

# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.info= f"{self.name}s age is {self.age}"


###################################################### Building Spheres ############################
# from math import pi


# class Sphere(object):

#     def __init__(self, r, m) -> None:
#         self.r = r
#         self.m = m

#     def get_radius(self):
#         return self.r

#     def get_mass(self):
#         return self.m

#     def get_volume(self):
#         v = 4 * pi / 3 * self.r ** 3
#         return round(v, 5)

#     def get_surface_area(self):
#         area = 4*pi * self.r**2
#         return round(area, 5)

#     def get_density(self):
#         den = self.m / (4 * pi / 3 * self.r ** 3)
#         return round(den, 5)


# ball = Sphere(2, 50)

# ball.get_radius()  # ,2, "Check radius"
# ball.get_mass()  # ,50, "Check mass"
# ball.get_volume()  # , 33.51032, "Check volume"
# ball.get_surface_area()  # ,50.26548, "Check area"
# ball.get_density()  # ,1.49208, "Check density"


############################################################ Python's Dynamic Classes #1 #############################


# def class_name_changer(cls, new_name):
#     if new_name[0].isupper() and new_name.isalnum():
#         cls.__name__ = new_name
#     else:
#         NameError("invalid clas name")
