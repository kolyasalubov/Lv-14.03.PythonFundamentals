from math import pi

class Sphere(object):
    def __init__(self, radius, mass):
        self.__radius = radius
        self.__mass = mass
    
    def get_radius(self):
        return self.__radius
    
    def get_mass(self):
        return self.__mass
    
    def volume(self):
        return round((4 / 3) * pi * self.__radius * self.__radius * self.__radius, 5)
    
    def get_surface_area(self):
        return round (4 * pi * self.__radius * self.__radius, 5)

    def get_density(self):
        volume = (4 / 3) * pi * self.__radius * self.__radius * self.__radius
        return round (self.__mass / volume, 5)
    
