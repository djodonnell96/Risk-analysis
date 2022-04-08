import risk_battle

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
