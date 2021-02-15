from Classes import Class
from Mob import mob
import random




Rogue = Class( 5, 20, 10, 10)
Warrior = Class( 1000, 10, 5, 15)
Wizzard = Class( 10, 5, 20, 5)



Zombie = mob( 5, 20, 10, 5, "zombie")
Bear = mob( 20, 10, 5, 15, "bear")
Bandit = mob( 10, 5, 20, 10, "bandit")





print("Hello and welcome to stereotypical rpg land")
name = input("What is your name young hero: ")
print("Hello " + name)
plyr_class = input("Choose your class (a)Rogue (b)Warrior (c) Wizzard: ")
if plyr_class == "a":
        Class = Rogue
if plyr_class == "b":
        Class = Warrior
if plyr_class == "c":
        Class = Wizzard


def run_encounter():
    lck1 = random.randint(1, 3)
    if lck1 == 1:
        mob = Bear
    if lck1 == 2:
        mob = Bandit
    if lck1 == 3:
        mob = Zombie
    print("A wild " + str(mob.Name) + " apeared")
    patck = float(Class.Strength/4)
    matck = float(mob.Strength/4)
    pmgk  = float(Class.Intelegence/4)
    mmgk = float(mob.Intelegence/4)
    while Class.Hp and mob.Hp >= 0:
        act = input("Choose your action, a)Attack b)Use magic c)Run away: ")
        if act == "a":
            mob.Hp -= patck
            print("You attack the " + str(mob.Name) +
                  ". The " + str(mob.Name) + " has " + str(mob.Hp) + " Hp")
        if act == "b":
            mob.Hp -= pmgk
            print("You cast a magic spell"
                  "The " + str(mob.Name) + " has " + str(mob.Hp) + " Hp")
        if act == "c":
            print("You run away")
            return
        Class.Hp -= matck
        print("The " + str(mob.Name) + " attacked you. " +
                  name + " has " + str(Class.Hp) + " Hp")
    if Class.Hp <= 0:
        print("You Died")
        return
    if mob.Hp <= 0:
        print("You killed The " + str(mob.Name))



run_encounter()
