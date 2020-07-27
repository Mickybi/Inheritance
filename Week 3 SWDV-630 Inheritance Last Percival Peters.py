# Week 3 SWDV-630 Inheritance Last Percival Peters.py

from Week 3 SWDV-630 Inheritance NameKeeper Percival Peters import *
from Week 3 SWDV-630 Inheritance TimeKeeper Percival Peters import *
from Week 3 SWDV-630 Inheritance Main Percival Peters import *

class TimeKeeper3(NameKeeper):
    def __init__(self, firstName, lastName, date, time):
        self.date = date
        self.time = time
        
    def showPunchOutTime():
        x = datetime.datetime.now()
        print(x)
        
 # ------------------------
 
    def Main():
        employeePunchIn = Timekeeper("John", "Doe", "11/21/2011", "06:30am")
        employeePunchOut = Timekeeper2("John", "Doe", "11/21/2011", "10:30am")
         
    #method call
    testMethod(employeePunchIn, employeePunchOut)
    
# Declaration
    def testMethod(employeePunchIn, employeePunchOut):
        print("John Doe has clocked in at 06:30am on 11/21/2011")
        print("John Doe has clocked out at 10:30am on 11/21/2011")


# Class invocation
    Main()
    