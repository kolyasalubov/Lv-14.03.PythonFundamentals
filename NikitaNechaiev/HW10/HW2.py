class Human:
    '''
    This is class Human
    Ще я зовсім не зрозумів завдання
    '''


    def __init__(self,name) -> None:
        self.name = name
    def greetings(self):
        print(f'Greetings {self.name}.')

    @classmethod
    def species(self):
        return 'Homosapiens.'
    @classmethod
    def arbitary_message(self):
        return 'Arbitrary message.'
    
user = Human('Jack')
user.greetings()
print(Human.species())
print(Human.arbitary_message())