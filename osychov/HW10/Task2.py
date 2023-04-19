class Human:
    species = "Homosapiens"
    
    def __init__(self, name):
        self.name = name
        
    def print_greetings(self):
        return f"Hello!!! I'm {self.name} :)"
    
    def species_print(self):
        return f"{self.name} is a {Human.species}"
    
    @staticmethod
    def message(name):
        return f"{str(name)} , You're amazing!"
        
Alex = Human("Alex")
print(Alex.print_greetings())
print(Alex.species_print())
print(Alex.message("Alex"))
