from abc import ABC
from abc import abstractmethod

class Employee:
    def __init__(self):
        self.name= ""
    
    def display(self):
        print(self.name)
    
class HourlyEmployee(Employee):
    def __init__(self):
        super().__init__()
        self.hourly_wage=0

    def display(self):
        print("{}  is a hourly employe which gain - ${}/hour".format(self.name, self.hourly_wage))
    
class SalaryEmployee(Employee):
    def __init__(self):
        self.salary=0

    def display(self):
        print("{} is a salary employe which gain- ${}/year".format(self.name,self.salary))
    
def main():
    employees = []
    usr_input= ""
    while usr_input != "q":
        print("For salary employee pres s\n For an hourly employee pres h\n To quit press q")
        usr_input = input("Enter your option: ")
        if usr_input == "s":
            new_s_emp= SalaryEmployee()
            new_s_emp.name = input("Enter Name: ")
            new_s_emp.salary = input("Enter salary: ")
            employees.append(new_s_emp)
        elif usr_input == "h":
            new_h_emp = HourlyEmployee()
            new_h_emp.name = input("Enter name: ")
            new_h_emp.hourly_wage = input("Enter hourly_wage: ")
            employees.append(new_h_emp)
    for employee in employees:
        employee.display()


if __name__ == "__main__":
    main()


    