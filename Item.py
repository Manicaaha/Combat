import random

class Item:
    def __init__(self, name, dmg, critDMG, critChance) -> None:
        self.name = name
        self.dmg = dmg
        self.critDMG = critDMG
        self.critChance = critChance

    def Use(self):
        fullDmg = self.dmg
        randChance = random.randint(0,100)
        if self.critChance >= randChance:
            fullDmg += self.critDMG
        return fullDmg
    
    def ShowStats(self):
        print(self.name, self.dmg,"+", self.critDMG,"crit", self.critChance, "%")

I1 = Item("Sword", 10.0, 5.0, 5)