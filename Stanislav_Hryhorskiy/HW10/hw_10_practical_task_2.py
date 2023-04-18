# *** Practical task 2 ***
# Create a class Human, everyone has a name,
# create a method in the class that displays
# a welcome message to each person. Create a class
# method in the class that returns information
# that it is a species of "Homosapiens". And in the
# class create a static method that returns an
# arbitrary message.


class Human:
    TYPE = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def get_welcome_message(self):
        return f"Hello, dear {self.name}! You belong to the '{self.__class__.__name__}' class."

    @classmethod
    def get_human_species(cls):
        return f"The class '{cls.__name__}' belongs " \
               f"to the species of '{cls.TYPE}'."

    @staticmethod
    def get_arbitrary_message():
        return "Special cases aren't special enough to break the rules!!!"


if __name__ == "__main__":
    user_name = input("Enter your name: ").capitalize()
    new_human = Human(user_name)
    print(new_human.get_welcome_message())
    print(new_human.get_human_species())
    print(new_human.get_arbitrary_message())
