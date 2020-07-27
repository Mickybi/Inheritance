# Week 3 SWDV-630 Inheritance TimeKeeper Percival Peters TimeKeeper.py

from Week 3 SWDV-630 Inheritance NameKeeper Percival Peters import *

class TimeKeeper(NameKeeper):
    def __init__(self, firstName, lastName, date, time):
        self.date = date
        self.time = time
        
    NameKeeper.__init__(self, firstName, lastName)
    
    def punchIn():
        # attempting to simulate punching in by using return statement
        return "You have punched in at" + x + "time!"
        
        