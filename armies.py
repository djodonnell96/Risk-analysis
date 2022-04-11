import random
from operator import attrgetter

class Soldier:
    active = True
    #A soldier makes up an army, and consists of their dice roll and a flag if they are active
    def __init__(self):
        roll = 0 #By default, hasn't rolled yet"
        active = True #Default status for a soldier"

    


    #When the soldier engages in battle, set it's roll to a random dice roll"
    def engage(self):
        self.roll = random.randint(1,6)
        
    #When the soldier is defeated, set their status to inactive/false"
    def defeated(self):
        self.active = False
        
    #Displaying Soldier values to command prompt
    def printSoldier(self):
        print(self.roll, " ", self.active)

class Army:
    
    #Constructing the army. Checks if valid size, if valid then creates the army
    def __init__(self, s = None):
        self.thisArmy = []

        # Checking if we are to create an empty army or an army with soldier
        if s == None:
            return
        else:
            self.size = s
            
        # Check for valid army size, create army if valid
        
        if (self.size < 1) or (self.size > 3): #Check for valid army size"
            print("Please enter an army size between 1 and 3")
        else :#Create an army(array) of s soldiers
            for x in range(self.size): # check indexing - I might have thought of this is 1 indexing
                newSoldier = Soldier()
                self.thisArmy.append(newSoldier)

    #Engage the army in battle aka setting dice rolls for each soldier
    def engage(self):
        for s in self.thisArmy:
            s.engage()

    #Display roll and status for each soldier in the army
    def armyStatus(self):
        for s in self.thisArmy:
            s.printSoldier()

    # sorting the armies by rolls highest to lowest
    def sort(self):
        self.thisArmy.sort(key=attrgetter('roll'),  reverse=True)
                
        
        


        


            
        
