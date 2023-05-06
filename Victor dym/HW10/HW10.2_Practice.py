class Human():
    def __init__(self, name):
        self.name = name

    def Hi_method(self):
        print(f"Hello {self.name}")

    @classmethod
    def info(cls):
        print(f" it is a Homosapiens")

    @staticmethod
    def random_message():
        print("Hey, have a nice day!")

hum = Human("Andrew")

hum.Hi_method()
hum.info()
hum.random_message()