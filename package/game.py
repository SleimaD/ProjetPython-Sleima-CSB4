from package.characters import Hero, Enemy
from package.items import Item, Inventory


import random       


class Game:
    def __init__(self):
        self.hero = None
        self.distance_to_boss = random.randint(8, 12) 
        self.current_distance = 0


    def start_game(self):
        print("\n----------------👋Helloo👋-----------------")
        print("- Welcome to the 👾WandelGame👾 ! -")
        print(" -    !!      Let's play    !!   -")
        print("-------------------------------------")
        hero_name = input("\n (❁´◡`❁) Now, Enter your hero's name🦸🏽: ")
        while True: 
            try:
                hero_class = int(input("Choose a category (1. Warrior🪖 , 2. Mage🧙 , 3. Archer🏹): "))
                if hero_class in [1, 2, 3]:
                    break 
                else:
                    print("Enter a valid option. Choose 1, 2, or 3.")
            except ValueError:
                print("Please enter a numerical value. Choose 1, 2, or 3.")
        if hero_class == 1:
            class_name = "Warrior"
        elif hero_class == 2:
            class_name = "Mage"
        else:
            class_name = "Archer"

        
        # Create the hero object with randomized stats
        self.hero = Hero(hero_name, hero_class, 100, random.randint(20, 30), 15)
        self.main_menu()


    def main_menu(self):
        while self.hero.is_alive():
            print("\n Main Menu🏠 :")
            print("1. Explore Forest🌳")
            print("2. Visit Village🏙️")
            print("3. Check Stats🧮")
            print("4. Check Inventory🎒")
            print("5. Quit Game 🚶")
            choice = input("Choose an option: ")
            if choice == '1':
                self.explore_forest()
            elif choice == '2':
                self.visit_village()
            elif choice == '3':
                self.hero.display_stats()
            elif choice == '4':
                self.check_inventory()
            elif choice == '5':
                print("\n Thank you for playing!") 
                break  
            else:
                print("\n Invalid choice.")
                
    
    def explore_forest(self):
        while True:
            print(f"\n Exploring the forest... You are now {self.current_distance} km from the start.")
            if self.current_distance == self.distance_to_boss:
                print("\n OPOPOP ! You've encountered the Boss!")
                self.encounter_boss()
                if not self.hero.is_alive():
                    print("\n You have been defeated by the Big Boss!")
                    break
                else:
                    print("\n You have defeated the Big Boss! You can continue exploring or return to the village.")
            
            print("\nWould you like to:")
            print("1. Continue exploring🌳")
            print("2. Return to main menu🏠")
            print("3. Check inventory🎒")
            print("4. View stats🧮")
            choice = input("Enter your choice (1-4): ")
            
            if choice == '1':
                self.current_distance += 1
                event = random.choice(["combat", "find", "nothing"])
                if event == "combat":
                    enemy = self.generate_enemy()
                    self.combat(self.hero, enemy)
                    if not self.hero.is_alive():
                        print("\n You have been defeated in battle!")
                        break
                elif event == "find":
                    self.random_find()
                elif event == "nothing":
                    print("\n Nothing happens...keep moving")
            elif choice == '2':
                self.current_distance = 0
                print("\n Returning to the main menu...")
                break
            elif choice == '3':
                self.check_inventory()
                item_name = input("Enter the item name to use or 'cancel' to return: ")
                if item_name.lower() == 'cancel':
                    continue
                self.use_item(item_name)
            elif choice == '4':
                self.hero.display_stats()
            else:
                print("\n Invalid choice, please choose again.")


    def use_item(self, item_name):
        #? use the item from the hero's inventory
        if self.hero.inventory.use_item(item_name, self.hero):
            print(f"Used {item_name}.")
        else:
            print("Item not found or not usable right now.")


    def encounter_boss(self):
        boss = Enemy("Big Boss", 300, 30, 20, 500, 1000) 
        self.combat(self.hero, boss)
        if not boss.is_alive():
            print("Congratulations! You have defeated the Big Boss and completed your quest!")



    def visit_village(self):
        print("\n Heeyy Welcome to the village. Here you can rest or buy items. 🤭")
        while True:
            print("\nVillage Menu:")
            print("1. Sleep at the inn (Costs 10 Gold)💤")
            print("2. Shop🛒")
            print("3. Return to Main Menu🏠")
            choice = input("Choose an option: ")
            if choice == '1':
                if self.hero.gold >= 10:
                    self.hero.hp = self.hero.max_hp
                    self.hero.gold -= 10
                    print("\n You are fully rested.")
                else:
                    print("\n Not enough gold to sleep at the inn.💔")
            elif choice == '2':
                self.shop()
            elif choice == '3':
                break
            else:
                print("\n Invalid choice.💔")


    def check_inventory(self):
        print("\n Inventory🎒:")
        for item in self.hero.inventory.items:
            print(item.name)
        print(f"Gold: {self.hero.inventory.gold}")


    def combat(self, hero, enemy):
        print(f" \n  Encountering : 🤜{enemy.name}🤛 ")
        while hero.is_alive() and enemy.is_alive():
            hero.display_stats()
            enemy.display_stats()
            action = input("\n Choose an action: Attack (a)👊 / Use Item (i)🧰 : ")
            if action == 'a': 
                self.attack(hero, enemy)
                if not enemy.is_alive():
                    print(f"{enemy.name} defeated!🥳")
                    hero.exp += enemy.exp_reward
                    hero.gold += enemy.gold_reward
                    if enemy.name == "Big Boss":
                        print("Yaaay You have won the game by defeating the Big Boss!🥳")
                        exit() 
                    return
            elif action == 'i':
                item_name = input("Enter the item name to use: ")
                if not hero.inventory.use_item(item_name, hero):
                    print("Item not found or not applicable.💔")
            if enemy.is_alive():
                self.attack(enemy, hero)
                if not hero.is_alive():
                    print("Oh no 🥺 You have been defeated!💔")
                    break


    def attack(self, attacker, defender):
        damage_reduction = defender.defense / (defender.defense + 60) 
        damage = max(1, int(attacker.attack * (1 - damage_reduction)))
        defender.hp -= damage
        print(f"\n {attacker.name} attacks {defender.name} for {damage} damage!👊")


    def generate_enemy(self):
        enemy_names = ['Goblin', 'Troll', 'Ninja']
        name = random.choice(enemy_names)
        hp = random.randint(50, 100)
        attack = random.randint(5, 15)
        defense = random.randint(5, 10)
        exp_reward = random.randint(5, 15)
        gold_reward = random.randint(10, 50)
        return Enemy(name, hp, attack, defense, exp_reward, gold_reward)

    
    def random_find(self):
        finds = ['gold', 'item', 'exp']
        result = random.choice(finds)

        if result == 'gold':
            amount = random.randint(10, 50)
            self.hero.inventory.gold += amount
            print(f"hey check, You found {amount} gold ⭐!")
        elif result == 'item':
            item = Item("Potion")
            self.hero.inventory.add_item(item)
            print("hey check, You found a Potion ⚗️ !")
            self.hero.hp = min(self.hero.hp + 20, self.hero.max_hp)
        elif result == 'exp':
            exp_amount = random.randint(5, 15)
            self.hero.exp += exp_amount
            print(f"check this, You gained {exp_amount} EXP 🪙 !")

    