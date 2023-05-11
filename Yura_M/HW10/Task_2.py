class Human():
    def __init__(self, name) -> None:
        self.name = name
        print(f"Hello, {self.name}! ")

    def specific(self):
        return f"{self.name} is kind Homosapiens"

    @staticmethod
    def arbitrary_message(name):
        return f"{(name)} , You're amazing!"


if __name__ == '__main__':
    Yura = Human('Yura')
    print(Yura.specific())
    print(Yura.arbitrary_message("Andriy"))
