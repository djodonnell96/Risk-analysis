import random

class Soldier:
    #A soldier makes up an army, and consists of their dice roll and a flag if they are active"
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
    size = 0
    thisArmy = []

    #Constructing the army. Checks if valid size, if valid then creates the army
    def __init__(self,s):
        self.size = s
        if (self.size < 1) or (self.size > 3): #Check for valid army size"
            print("Please enter an army size between 1 and 3")
        else :#Create an army(array) of s soldiers"
            for x in range(self.size):
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

class Battle:
    attacker = Army(1)
    defender = Army(1)
    
    def __init__(self, attacker, defender):
        self.attacker = attacker
        if defender.size > 2:
            print("Defending armies can be a maximum size of 2")
        else:
            self.defender = defender

    def engage(self):
        attacker.sort(reverse=True)
        defender.sort(reverse=True)
        
        

print("Creating a new army, all should be boilerplate")
testArmy = Army(2)
testArmy.armyStatus()

print("\nEngaging the army, should now show new values for rolls")
testArmy.engage()
testArmy.armyStatus()

print("\nInvalid army size test")
invalidArmy = Army(55)

            
        
