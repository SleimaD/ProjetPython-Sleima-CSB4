import random

class Item:
    def __init__(self, name, effect=None):
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
                if item.effect is not None:
                    item.effect(hero)  #? Call the effect only if it is not None
                self.items.remove(item)
                return True
        return False