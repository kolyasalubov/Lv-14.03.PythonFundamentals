class Human():
    def __init__(self, name):
        self.name = name
    def welcome_message(self):
        return f'Hello, {self.name}!'
    @classmethod
    def show_species(cls):
        return f'{cls.__name__} is a species of "Homosapiens"'
    @staticmethod
    def static_message():
        return 'Human is in developing...'
