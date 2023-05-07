class Human:
    species = "Homosapiens"  

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, my name is {self.name}!")

    @classmethod
    def get_species(cls):
        return cls.species

    @staticmethod
    def get_arbitrary_message():
        return "This is a static message."


human1 = Human("Alice")
human2 = Human("Bob")

human1.say_hello()   
human2.say_hello()   
print(Human.get_species())             
print(Human.get_arbitrary_message())  
