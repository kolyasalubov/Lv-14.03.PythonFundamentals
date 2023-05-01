class Employee:
    num = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.num += 1

    @classmethod
    def counter(cls):
        return f"Total num of employees:{cls.num}"

    def info(self):
        return f"{self.name.title()} earns {self.salary} $."


anna = Employee('Anna', '40000')
kate = Employee("Kate", "12000")

print(Employee.counter())

print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)
