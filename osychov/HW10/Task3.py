class Employee:
    count = 0
    def __init__(self, name , salary):
        self.name = name
        self.salary = salary
        Employee.count +=1
    
    def num_of_employ():
        return f"The company has {Employee.count} employees"

    def get_information(self):
        return f"Employee {self.name} has {self.salary} salary"
    
    @staticmethod
    def all_employees():
        for empl in employees:
            print(empl.get_information())

employees = [Employee("Alex", 2000), Employee("Oleg", 3000),Employee("Igor", 4000)]   

def main():
    print(Employee.num_of_employ()) #number of employees
    Employee.all_employees()                
    print(Employee.__base__)
    print(Employee.__dict__)
    print(Employee.__name__)
    print(Employee.__module__)
    print(Employee.__doc__)
    
main()
        
  