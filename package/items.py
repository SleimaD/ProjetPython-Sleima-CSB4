import random

class Item:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

class Inventory:
    def __init__(self):
        self.items = []
        self.gold = 0   

    def add_item(self, item):
        self.items.append(item)

    def use_item(self, item_name, hero):
        for item in self.items:
            if item.name == item_name:
                item.effect(hero)
                self.items.remove(item)
                return True
        return False
