from cgi import test
import armies
import battle

#Test all valid and edge case Army sizes

#Valid size army tests

validTestingArmies = []
army1 = armies.Army(1)
army2 = armies.Army(2)
army3 = armies.Army(3)

validTestingArmies.append(army1)
validTestingArmies.append(army2)
validTestingArmies.append(army3)

#Expect everything to be boilerplate
print("All armies set to default:")
for army in validTestingArmies:
    army.armyStatus()

#Roll each soldier's die
for army in validTestingArmies:
    army.engage()

# Sew new results
print("All armies have now rolled")
for army in validTestingArmies:
    army.armyStatus()

# Test defeat function
#for army in validTestingArmies:
#    army.defeated()

#All armies have been defeated
#print("All armies have now been defeated:")
#for army in validTestingArmies:
#    army.armyStatus()

# Testing pitting armies against one another
print("Pitting Army 1 and Army 2 against one another")
testBattle = battle.Battle(army2,army1)
testBattle.engage()

print("Army 1 battle results:")
validTestingArmies[1].armyStatus()
print("Army 2 battle results:")
validTestingArmies[2].armyStatus()