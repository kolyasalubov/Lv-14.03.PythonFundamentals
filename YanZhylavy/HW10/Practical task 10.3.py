class Employees:
  '''
  A class that contains information about employees
  '''
  number_of_employees = 0
  def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
        Employees.number_of_employees +=1
    
  def __del__(self):
        Employees.number_of_employees -=1

  def total_employees(self):
        print(Employees.number_of_employees)

  def employee_info(self):
        return self.name, self.__salary

print(Employees.__base__)
print(Employees.__dict__)
print(Employees.__name__)
print(Employees.__module__)
print(Employees.__doc__)
      
  