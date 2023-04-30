class Employee:
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = int(salary)
        Employee.count += 1

    def information_employees(self):
        return f"{self.name} worker has a salary {self.salary}$"

    @classmethod
    def counter_employees(cls):
        return f"The company has {cls.count} employees"


worker1 = Employee("Oleg", 2346)
worker2 = Employee("Lesha", 5405)
worker3 = Employee("Vasya", 4973)
worker4 = Employee("Bodya", 2347)

print(f"{Employee.counter_employees()}\n")
print(f"{worker1.information_employees()}\n{worker2.information_employees()}\n{worker3.information_employees()}\n"
      f"{worker4.information_employees()}\n")
print(f"\nThe base class from which the employee class is inherited is {Employee.__base__}")
print(f"The class Employee namespaces: {Employee.__dict__}")
print(f"The class name is {Employee.__name__}")
print(f"The module name in which the class is defined: {Employee.__module__}")
print(f"The documentation bar: {Employee.__doc__}\n")
