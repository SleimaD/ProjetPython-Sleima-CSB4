import random
from package.items import Inventory 


class Character:
    def __init__(self, name, hp, attack, defense, exp=0, level=1):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.defense = defense
        self.exp = exp
        self.level = level

    def is_alive(self):
        return self.hp > 0 #? Return True if HP is above 0, False otherwise

    def display_stats(self):
        print(f"\n {self.name} - your hero's HP: {self.hp}/{self.max_hp}, it's Level: {self.level}, it's EXP: {self.exp}")



class Hero(Character):
    def __init__(self, name, job, hp, attack, defense, exp=0, level=1, gold=0):
        super().__init__(name, hp, random.randint(20, 30), min(defense, 15), exp, level) #? Call the parent class constructor
        self.job = job
        self.gold = gold
        self.inventory = Inventory() #? Create an inventory for the hero



class Enemy(Character):
    def __init__(self, name, hp, attack, defense, exp_reward, gold_reward):
        super().__init__(name, hp, attack, defense) #? Call the parent class constructor
        self.exp_reward = exp_reward #? The amount of exp gained by defeating the enemy
        self.gold_reward = gold_reward #? The amount of gold gained by defeating the enemy

