from package.characters import Hero, Enemy
from package.items import Item, Inventory


import random       


class Game:
    def __init__(self):
        self.hero = None #? Initialize hero as None before starting the game
        self.distance_to_boss = random.randint(8, 12) #? Randomly set the distance to the boss between 8 and 12
        self.current_distance = 0 #? Initialize the distance travelled to 0


    def start_game(self):
        print("\n----------------👋Helloo👋-----------------")
        print("- Welcome to the 👾WandelGame👾 ! -")
        print(" -    !!      Let's play    !!   -")
        print("-------------------------------------")
        hero_name = input("\n (❁´◡`❁) Now, Enter your hero's name🦸🏽: ")
        while True: 
            try:
                hero_class = int(input("\n Choose a category (1. Warrior🪖 , 2. Mage🧙 , 3. Archer🏹): "))
                if hero_class in [1, 2, 3]:
                    break #? Break loop if a valid option is chosen
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

        
        #? Create the hero object with randomized stats
        self.hero = Hero(hero_name, hero_class, 100, random.randint(20, 30), 15)
        self.main_menu() #? Enter the main menu of the game


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
                self.encounter_boss() #? Trigger le boss encounter
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
                self.current_distance += 1  #? Increment distance if continuing exploration
                event = random.choice(["combat", "find", "nothing"]) #? Randomly choose an event
                if event == "combat":
                    enemy = self.generate_enemy() #? Generate a random enemy
                    self.combat(self.hero, enemy) #? Initiate combat with the enemy
                    if not self.hero.is_alive():
                        print("\n You have been defeated in battle!")
                        break
                elif event == "find":
                    self.random_find()   #? Trigger a random find event
                elif event == "nothing":
                    print("\n Nothing happens...keep moving")
            elif choice == '2':
                self.current_distance = 0   #? Reset distance and return to main menu
                print("\n Returning to the main menu...")
                break
            elif choice == '3':
                self.check_inventory()
                item_name = input("Enter the item name to use or 'cancel' to return: ")
                if item_name.lower() == 'cancel':
                    continue   #? Return to previous menu if canceled
                self.use_item(item_name)
            elif choice == '4':
                self.hero.display_stats()
            else:
                print("\n Invalid choice, please choose again.")


    def use_item(self, item_name):
        #? use the item from the hero's inventory
        if self.hero.inventory.use_item(item_name, self.hero):
            print(f"\n Used {item_name}.")
        else:
            print("\n Item not found or not usable right now.")


    def encounter_boss(self):
        boss = Enemy("Big Boss", 300, 30, 20, 500, 1000)  #? Creation of boss enemy
        self.combat(self.hero, boss)  #? Initiate combat with the boss
        if not boss.is_alive():
            print("\n Youhouuu  Congratulations! You have defeated the Big Boss and completed your quest!")



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
                    self.hero.hp = self.hero.max_hp   #? Restore hero's health fully if enough gold
                    self.hero.gold -= 10              #? Deduct cost for sleeping at the inn
                    print("\n You are fully rested.")
                else:
                    print("\n Not enough gold to sleep at the inn.💔")
            elif choice == '2':
                self.shop()  #? Enter shop
            elif choice == '3':
                break  #? Return to main menu
            else:
                print("\n Invalid choice.💔")


    def check_inventory(self):
        print("\n Inventory🎒:")
        for item in self.hero.inventory.items:
            print(item.name)  #? List each item in the inventory
        print(f"\n Gold: {self.hero.inventory.gold}")


    def combat(self, hero, enemy):
        print(f" \n  Encountering : 🤜{enemy.name}🤛 ")
        while hero.is_alive() and enemy.is_alive():
            hero.display_stats()   #? Display hero's stats
            enemy.display_stats()   #? Display enemy's stats
            action = input("\n Choose an action: Attack (a)👊 / Use Item (i)🧰 : ")
            if action == 'a': 
                self.attack(hero, enemy)  #? Initiate attack
                if not enemy.is_alive():
                    print(f"\n Youhouuu {enemy.name} defeated!🥳")
                    hero.exp += enemy.exp_reward   #? reward exp points
                    hero.gold += enemy.gold_reward #? reward gold
                    if enemy.name == "Big Boss":
                        print("\n Yaaay You have won the game by defeating the Big Boss!🥳")
                        exit()  #? Exit game
                    return
            elif action == 'i':
                item_name = input("Enter the item name to use: ")
                if not hero.inventory.use_item(item_name, hero):
                    print("\n Item not found or not applicable.💔")
            if enemy.is_alive():
                self.attack(enemy, hero)   #? Enemy attacks hero
                if not hero.is_alive():
                    print("\n Oh no 🥺 You have been defeated!💔")
                    break


    def attack(self, attacker, defender):
        damage_reduction = defender.defense / (defender.defense + 60)   #? Calculate damage reduction based on defense
        damage = max(1, int(attacker.attack * (1 - damage_reduction)))  #? Calculate damage after reduction
        defender.hp -= damage   #? Deduct damage from defender's health
        print(f"\n {attacker.name} attacks {defender.name} for {damage} damage!👊")


    def generate_enemy(self):
        enemy_names = ['Goblin', 'Troll', 'Ninja']
        name = random.choice(enemy_names)   #? Randomly choose an enemy name
        hp = random.randint(50, 100)
        attack = random.randint(5, 15)
        defense = random.randint(5, 10)
        exp_reward = random.randint(5, 15)
        gold_reward = random.randint(10, 50)
        return Enemy(name, hp, attack, defense, exp_reward, gold_reward)    #? Return the generated enemy

    
    def random_find(self):
        finds = ['gold', 'item', 'exp']
        result = random.choice(finds) #? randomly choose what the hero finds 

        if result == 'gold':
            amount = random.randint(10, 50) #? randomly generate the amount the hero finds
            self.hero.inventory.gold += amount #? add gold to the hero's inventory
            print(f"\n hey check, You found {amount} gold ⭐!")
        elif result == 'item':
            item = Item("Potion")
            self.hero.inventory.add_item(item) #? add item to hero's inventory
            self.hero.hp = min(self.hero.hp + 20, self.hero.max_hp) #? increase hero's health
            print("\n hey check, You found a Potion ⚗️ !")
        elif result == 'exp':
            exp_amount = random.randint(5, 15) #? generate a random exp amount
            self.hero.exp += exp_amount #? add exp to hero's total
            print(f"\n check this, You gained {exp_amount} EXP 🪙 !")
    
        
    def shop(self):
        
        items_for_sale = {
            'Potion': 5,
            'Super Potion': 20
        }

        
        print("\n Items for sale:")
        for item, price in items_for_sale.items():
            print(f"{item}: {price} gold")

        
        while True:
            buy_item = input("\n Which item would you like to buy? (Type the exact name or 'cancel' to exit): ")
            if buy_item.lower() == 'cancel':
                print("\n Exiting shop.")
                break  

          
            if buy_item in items_for_sale:
                item_price = items_for_sale[buy_item] #? get price of choosen item 
                if self.hero.inventory.gold >= item_price:
                    self.hero.inventory.gold -= item_price  #? deduct the price of item from hero's gold
                    self.apply_effect(buy_item)   #? Apply effect of the bought item
                    print(f"\n Bought {buy_item}.")
                    break 
                else:
                    print("\n Not enough gold.")
            else:
                print("\n Item not found, please try again.")

    def apply_effect(self, item_name):
       
        if item_name == 'Potion':
            self.hero.hp = min(self.hero.hp + 20, self.hero.max_hp) #? increase hero's health by  20
            print(f"\n {self.hero.name}'s health increased to {self.hero.hp}.")
        elif item_name == 'Super Potion':
            self.hero.hp = self.hero.max_hp #? fully restore hero's health
            print(f"\n {self.hero.name}'s health fully restored to {self.hero.hp}.")


    