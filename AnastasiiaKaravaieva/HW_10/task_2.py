class Human:

    def __init__(self, name):
        self.name = name.title()

    def greeting(self):
        print(f"Hi,{self.name}!")

    def what_a_species(self):
        print(f"{self.name}, you are the Homosapiens.")

    @staticmethod
    def message():
        print("I love people.")