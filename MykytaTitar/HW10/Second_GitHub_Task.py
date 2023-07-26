class Human:
    species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def welcome(self):
        return f"Hello, My name is {self.name}"

    @classmethod
    def classmethod(cls):
        return f"Your species is {Human.species}"

    @staticmethod
    def staticmethod(name):
        return f"Hi, my dear {str(name)}"


user = Human("Artem")

print(user.welcome())
print(user.classmethod())
print(user.staticmethod("Artem"))
