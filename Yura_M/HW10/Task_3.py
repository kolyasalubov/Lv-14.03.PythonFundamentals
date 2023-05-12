class Employess():
    count_employess = 0

    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary
        Employess.count_employess += 1

    def total_count_of_employees():
        return f"The company has {Employess.count_employess} employes"

    def inform_emp(self):
        return f"Employe {self.name} has {self.salary} salari"

    def __del__(self):
        Employess.count_employess -= 1


print(Employess.__base__)
print(Employess.__dict__)
print(Employess.__name__)
print(Employess.__module__)
print(Employess.__doc__)

if __name__ == '__main__':
    emp1 = Employess('Yura', 3000)
    emp2 = Employess('Andriy', 2500)
    emp3 = Employess('Igor', 5000)
    print(Employess.total_count_of_employees())
    print(Employess.inform_emp(emp3))
