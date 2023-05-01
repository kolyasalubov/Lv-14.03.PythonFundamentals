class Employee():
    """
    Employee class
    Fields:
        Name: str
        Salary: int
    Methods:
    employees_count(), display_information()
    """
    employees_counter = 0

    def __init__(self, name: str, salary: int):
        self.name = name
        self.salary = int(salary)
        Employee.employees_counter += 1
        print(f"The base class from which the employee class is inherited is {Employee.__base__} \n")
        print(f"The class Employee namespaces: {Employee.__dict__}\n")
        print(f"The class name is {Employee.__name__}\n")
        print(f"The module name in which the class is defined: {Employee.__module__}\n")
        print(f"The documentation bar: \n {Employee.__doc__}")
        
    def __del__(self):
        Employee.employees_counter -= 1

    @classmethod
    def employees_count(cls):
        return cls.employees_counter

    def display_information(self):
        return f"{self.name} is a employee that has {self.salary} salary."


      