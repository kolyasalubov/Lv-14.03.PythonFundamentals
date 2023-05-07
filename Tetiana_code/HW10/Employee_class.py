class Employee:
    num_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.num_employees += 1

    def display_employee_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

    @classmethod
    def display_num_employees(cls):
        print(f"Total number of employees: {cls.num_employees}")

print(Employee.__base__)     
print(Employee.__dict__)     
print(Employee.__name__)     
print(Employee.__module__)  
print(Employee.__doc__)  
