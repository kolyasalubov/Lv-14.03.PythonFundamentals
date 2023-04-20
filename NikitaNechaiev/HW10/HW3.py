class Employee:
    '''
    This is Emloyee class
    '''
    counter = 0
    def __init__(self,name,salary) -> None:
        self.name = name
        self.salary = salary
        Employee.emp_count += 1
    emp_count = 0    
    
    def display(self):
        print(f'Hire Details:\n Employee: {self.name}\n Salary: {self.salary}$\n--------------')


user1 = Employee("Homer Simpson",500)
user1.display()
user2 = Employee("Stepan Bandera",1100)
user2.display()
user3 = Employee("Peter Griffin",600)
user3.display()
user4 = Employee("Ricky Morty",450)
user4.display()
print(f'Total hired {Employee.emp_count} employees.')

print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)