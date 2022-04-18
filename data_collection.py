import armies
import battle

battleResults = []

attacker = armies.Army(2)
defender = armies.Army(2)
endlessBattle = battle.Battle(attacker,defender)

for i in range(10):
    endlessBattle.engage()
    battleResults.append(endlessBattle.armiesInfo())
    attacker = armies.Army(2)
    defender = armies.Army(2)

for s in battleResults:
    print(s)