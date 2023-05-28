import random
import os
import time
from Item import *
from Player import *

class combat:
    def __init__(self) -> None:
        self.team1 = []
        self.team2 = []
    def AddPlayer(self, player):
        self.team1.append(player)
    
    def ShowTeam(self, team):
        i = 0
        if team == 1:
            for player in self.team1:
                print(i,": ",end="")
                player.ShowStats()
                i+=1
        else:
            for player in self.team2:
                print(i,": ",end="")
                player.ShowStats()
                i+=1

    def AddOpponent(self, player):
        self.team2.append(player)


    def save(self):
        with open("save.txt", "w") as file:
            file.write(f"{len(self.team1)} {len(self.team2)}\n")

            for player in self.team1:
                file.write(
                    f"{player.name} {player.dmg} {player.HP} {player.exp} "
                    f"{player.item.name} {player.item.dmg} {player.item.critDMG} {player.item.critChance}\n"
                )

            for opponent in self.team2:
                file.write(
                    f"{opponent.name} {opponent.dmg} {opponent.HP} {opponent.exp} "
                    f"{opponent.item.name} {opponent.item.dmg} {opponent.item.critDMG} {opponent.item.critChance}\n"
                )

        print("Game saved successfully")

    def load(self):
        if not os.path.exists("save.txt"):
            print("No saved game found")
            return

        with open("save.txt", "r") as file:
            lines = file.readlines()

            counts = [int(p) for p in lines[0].split()]
            player_count = counts[0]

            for line in lines[1 : 1 + player_count]:
                player_data = line.split()
                name = player_data[0]
                dmg = int(player_data[1])
                HP = int(player_data[2])
                exp = int(player_data[3])
                item_name = player_data[4]
                item_dmg = float(player_data[5])
                item_critDMG = float(player_data[6])
                item_critChance = float(player_data[7])

                item = Item(item_name, item_dmg, item_critDMG, item_critChance)
                player = Player(name, dmg, HP, exp, item)
                self.team1.append(player)

            for line in lines[1 + player_count:]:
                opponent_data = line.split()
                name = opponent_data[0]
                dmg = float(opponent_data[1])
                HP = float(opponent_data[2])
                exp = float(opponent_data[3])
                item_name = opponent_data[4]
                item_dmg = float(opponent_data[5])
                item_critDMG = float(opponent_data[6])
                item_critChance = float(opponent_data[7])

                item = Item(item_name, item_dmg, item_critDMG, item_critChance)
                opponent = Player(name, dmg, HP, exp, item)
                self.team2.append(opponent)

        print("Game loaded successfully")

    
    def fight(self):
        while True:
            os.system("cls")
            self.ShowTeam(1)
            print("-------------------------------")
            self.ShowTeam(2)
            playerIndex = int(input("Pick Player: "))
            os.system("cls")
            self.team1[playerIndex].ShowStats()
            print("-------------------------------")
            self.ShowTeam(2)
            opponentIndex = int(input("Pick Opponent: "))
            os.system("cls")
            self.team1[playerIndex].ShowStats()
            print("-------------------------------")
            self.team2[opponentIndex].ShowStats()
            print("Players fighting...")
            time.sleep(3)
            playerDMG = self.team1[playerIndex].Attack()
            self.team2[opponentIndex].ModifyHP(playerDMG)
            print("Player deals: ", playerDMG, "damage to opponent")
            time.sleep(1)
            if self.team2[opponentIndex].HP > 0:
                self.team1[playerIndex].ModifyHP(self.team2[opponentIndex].dmg)
                print("Opponent deals", self.team2[opponentIndex].dmg)
            else:
                print("Opponent is dead")
                self.team2.pop(opponentIndex)
                self.team1[playerIndex].LevelUp()
            

            option = input("Continue? (y/n): ")

            if option.lower() == "":
                    continue
            elif option.lower() == "n":
                    self.save()  
                    break



c = combat()

load_option = input("Do you want to start a new game or load a saved game? (new (n) /load (l) ): ")
if load_option.lower() == "l":
    c.load()
else:

    c.AddPlayer(Player("Oskar", 10, 100, 0, Item("Sword", 30, 15, 30)))
    c.AddPlayer(Player("Martyna", 10, 100, 0, Item("Axe", 25, 20, 35)))
    c.AddOpponent(Player("Szymon", 10, 100, 0, Item("Keyboard", 10, 45, 60)))
    c.AddOpponent(Player("Julek", 10, 100, 0, Item("Axe", 25, 20, 35)))

c.fight()