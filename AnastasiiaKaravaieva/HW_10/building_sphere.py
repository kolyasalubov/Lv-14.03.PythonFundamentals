import math

class Sphere(object):
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
        
    def get_radius(self):
        return self.radius
    
    def get_mass(self):
        return self.mass
    
    def get_volume(self):
        volume = 4/3*math.pi*(self.radius**3)
        return round(volume, 5)
    
    def get_surface_area(self):
        surf_a = 4*math.pi*self.radius**2
        return round(surf_a, 5)
    
    def get_density(self):
        density = self.mass/ self.get_volume()
        return round(density, 5)
    