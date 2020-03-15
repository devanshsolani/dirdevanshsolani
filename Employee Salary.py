class Company:

    def __init__(self):
        self.cname = input("Enter Company Name: ")
        self.empid = input("Enter Employee ID: ")
        self.name = input("Enter Employee Name: ")
        self.qual = input("Enter Employee Qualification: ")
        self.designation = input("Enter Employee Designation: ")
        self.salary = int(input("Enter Employee Salary: "))


# Calculating the salary after doing all the operations
class Basic_salary:

    def __init__(self):
        self.TA = ((18 * self.salary) / 100)
        self.DA = ((17 * self.salary) / 100)
        self.HRF = ((25 * self.salary) / 100)
        self.EPF = ((10 * self.salary) / 100)
        self.net_salary = self.salary + self.TA + self.DA + self.HRF - self.EPF


# The concept of Multiple Inheritance
class Calculation(Company, Basic_salary):

    def __init__(self):
        Company.__init__(self)
        Basic_salary.__init__(self)
        print("TA: ", self.TA)
        print("DA: ", self.DA)
        print("HRF: ", self.HRF)
        print("EPF: ", self.EPF)
        print("Net Salary: ", self.net_salary)

Calculation()
