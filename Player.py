class Player:
    def __init__(self, name, dmg, HP, exp, item) -> None:
        self.HP = HP
        self.item = item
        self.name = name
        self.exp = exp
        self.dmg = dmg

    def ShowStats(self):
        print(self.name, end=" * ")
        print("dmg",self.dmg, end=" * ")
        print("HP",self.HP, end=" * ")
        print("exp",self.exp, end=" * ")
        self.item.ShowStats()
    
    def Attack(self):
        return self.dmg + self.item.Use() + self.exp
    
    def ModifyHP(self, mod):
        self.HP -= mod

    def LevelUp(self):
        self.exp += 1