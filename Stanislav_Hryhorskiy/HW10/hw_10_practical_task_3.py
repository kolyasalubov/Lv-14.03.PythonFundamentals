# *** Practical task 3 ***
# Create an employee class. Each employee has characteristics such as name and salary.
# The class should have a counter that calculates the total number of employees,
# as well as a method that prints the total number of employees and a method that
# displays information about each employee in particular, namely the name and salary.
# In addition to creating a class, display information about the base classes from
# which the employee class is inherited (__base__), the class namespace (__dict__),
# the class name (__name__), the module name in which the class is defined (__module__),
# the documentation bar (__doc__).

from pprint import pprint


class Employee:
    """
    Class describing the employee (has characteristics such as name and salary)
    """
    total_count = 0

    def __init__(self, name, salary):
        self.name = name.capitalize()
        self.salary = float(salary)
        self.__class__.total_count += 1
        self.count = self.total_count

    @classmethod
    def get_number_employees(cls):
        print(f"Total number of employees is {cls.total_count}.")

    def get_employee_information(self):
        print(f"Employee №{self.count}: "
              f"name {self.name}; salary {self.salary:.2f} $.")


if __name__ == "__main__":
    employee_list = []
    while True:
        info = input("Enter employee information (NAME and SALARY separated by a space): ").split()
        employee_list.append(Employee(info[0], info[1]))
        flag = input("To complete the data entry, enter 'end': ").lower()
        if flag == 'end':
            print(50*'*')
            break

    for item in employee_list:
        item.get_employee_information()
    Employee.get_number_employees()

    print(f"The class name that describe the employee is '{Employee.__name__}'.")
    print(f"The '{Employee.__name__}' class is inherited by '{Employee.__base__}'.")
    pprint(f"The '{Employee.__name__}' class namespace: {Employee.__dict__}")
    print(f"The module name in which the class '{Employee.__name__}' is defined: '{Employee.__module__}'.")
    print(f"The documentation bar of the '{Employee.__name__}' class: {Employee.__doc__}")
