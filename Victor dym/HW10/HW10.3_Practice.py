class Employee():
    """
    Here is a counter that counts how many people are there in the company - how many class instances are there
    The delete method that deletes 1 from counter each time the employee is deleted - the class instance is deleted
    Overall shows how many employees are there in the company
    Info provides info about the name and the salary of a specific employee

    """
    counter = 0

    def __init__(self, name, salary):
        Employee.counter += 1
        self.name = name
        self.salary = salary

    def __del__(self):
        Employee.counter -= 1

    def overall(self):
        print(Employee.counter)

    def info_employee(self):
        print(f"The name of employee: {self.name} and his salary is {self.salary}")


emp = Employee("Victor", 1200)
emp1 = Employee("Victor", 1300)

emp.overall()
emp.info_employee()
emp1.info_employee()
print(Employee.__doc__)
print(Employee.__base__)
print(emp.__class__.__name__)
print(Employee.__module__)
print(Employee.__dict__)