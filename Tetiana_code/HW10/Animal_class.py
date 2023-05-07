class Animal:
    def __init__(self, name, species, num_legs):
        self.name = name
        self.species = species
        self.legs = num_legs
        
    def make_sound(self):
        pass

class Mammal(Animal):
    def give_birth(self):
        pass
    
    def make_sound(self):
        return "Roar"
class Bird(Animal):
    def lay_eggs(self):
        pass
    
    def make_sound(self):
        return "Squawk"

class Reptile(Animal):
    def shed_skin(self):
        pass
    
    def make_sound(self):
        return "Hiss"