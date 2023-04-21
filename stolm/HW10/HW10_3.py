class Employee:

    """
    The class was created to enter employee data.
    There are name and salary fields.
    The total number of employees is also recorded.
    """

    counter = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        __class__.counter += 1

    def total_employees():
        return __class__.counter
    
    def info(self):
        return f"Name: {self.name} \tSalary: {self.salary}"
    

if __name__ == "__main__":

    staff_list = [] # Our list of employees
    active = True 

    while active: # Input the names and salaries of our emplyees
        name = input("Enter the name: ")
        salary = input(f"Enter the {name.title()}'s salsary: ")
        staff_list.append(Employee(name, salary))
        continue_work = int(input("Enter 1 if you want to continue working with the program, 0 if you want to quit: "))
        if continue_work == False:
            active = False

    for i in staff_list:
        print(i.info())
    
    print(f"\nThe total number of emplyes: {Employee.total_employees}")

    print(f"\nClass is inhetered by: {Employee.__base__}")
    print(f"\nThe class namespace: {Employee.__dict__}")
    print(f"\nThe class name: {Employee.__name__}")
    print(f"\nThe module name in which class is defined: {Employee.__module__}")
    print(f"\nThedocumentation bar: {Employee.__doc__}")