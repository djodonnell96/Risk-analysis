import armies

class Battle:
    # constructor, 
    def __init__(self, newAttackingArmy, newDefendingArmy):

        # check if attacker army size is between 1 and 3, if so continue on
        if newAttackingArmy.size < 1 or newAttackingArmy.size > 3:
            print("Attacking armies must contain 1-3 soldiers")
        else:
            self.attacker = newAttackingArmy

        # check if defending army size is 1 or 2, if so continue on
        if newDefendingArmy.size < 1 or newDefendingArmy.size > 2:
            print("Defending armies can be a maximum size of 2")
        else:
            self.defender = newDefendingArmy

    # As the game would go, roll each solder's die and sort in descending order
    def engage(self):
        self.attacker.engage()
        self.defender.engage()
        self.attacker.sort()
        self.defender.sort()

        # compare armies and set flags to defeated if necessary
        x = max(attacker.size,defender.size)

        # Comparing rolls for each soldier. Defender wins ties.
        for i in range(x):
            if defender.thisArmy[i].roll >= attacker.thisArmy[i].roll:
                attacker.thisArmy[i].defeated()
            elif defender.thisArmy[i].roll < attacker.thisArmy[i].roll:
                defender.thisArmy[i].defeated()

    def armiesInfo(self):
        print("Attacker Status:")
        self.attacker.armyStatus()
        print("Defender Status:")
        self.defender.armyStatus()


attacker = armies.Army(3)
defender = armies.Army(2)

newBattle = Battle(attacker,defender)

newBattle.engage()

newBattle.armiesInfo()
