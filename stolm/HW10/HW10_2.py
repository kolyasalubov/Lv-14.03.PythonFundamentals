class Human:
    def __init__(self, name):
        self.name = name

    
    def hello(self):
        return f"Hello, {self.name}!"
    
    @classmethod
    def info(self):
        return f"Type: Homosapiens!"

    @staticmethod
    def message(): 
        return f"This message was crated by @staticmethod!"
    

if __name__ == "__main__":
    name = input("Enter your name: ")
    human = Human(name)
    print(human.hello())
    print(human.info())
    print(human.message())
