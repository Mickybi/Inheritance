import datetime

# Week 3 SWDV-630 Inheritance NameKeeper Percival Peters.py

class NameKeeper:
    def __init__(self, firstName, lastName):
       self.firstName = firstName
       self.lastName = lastName
       
    def showEmployeeId():
        # attempting to print employee id with the return statement
        employeeId = input("What is your employee ID?(Six numbers) ")
        return employeeId
    
    p1 = Employee("John", "Doe")
    print(p1.firstName, p1.lastName)
    
    def showTodaysDate():
        x = datetime.datetime.now()
        print(x)
    
    

