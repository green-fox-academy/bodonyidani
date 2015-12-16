from display import print_skulls
from random import randint

class Player():
    def __init__(self = None,
        name = None,
        dexterity = None,
        maxhealth = None,
        currhealth = None,
        maxluck = None,
        currluck = None,
        inventory = ["SWORD", "LEATHER ARMOR"]
        ):
        self.name = name
        self.dexterity = dexterity
        self.maxhealth = maxhealth
        self.currhealth = currhealth
        self.maxluck = maxluck
        self.currluck = currluck
        self.inventory = inventory

    def set_name(self, name):
        self.name = name.upper()

    def set_initial_dexterity_health_luck(self, dexterity, maxhealth, maxluck):
        self.dexterity = dexterity
        self.maxhealth = maxhealth
        self.currhealth = maxhealth
        self.maxluck = maxluck
        self.currluck = maxluck

    def set_potion(self, potion):
        self.inventory = [self.inventory[0], self.inventory[1]]
        self.inventory.append(potion)

    def display_name(self):
        print(" NAME: " + str(self.name) + "\n")

    def display_starting_stats(self):
        print(" DEXTERITY: " + str(self.dexterity) + "\n")
        print(" HEALTH: " + str(self.maxhealth) + "\n")
        print(" LUCK: " + str(self.maxluck) + "\n")

    def display_starting_health(self):
        print(" STARTING (MAX) HEALTH: " + str(self.maxhealth) + "\n")

    def display_starting_luck(self):
        print(" STARTING (MAX) LUCK: " + str(self.maxluck) + "\n")

    def display_current_stats(self):
        print(" DEXTERITY: " + str(self.dexterity) + "\n")
        print(" HEALTH: " + str(self.currhealth) + "\n")
        print(" LUCK: " + str(self.currluck) + "\n")

    def display_dexterity(self):
        print(" DEXTERITY: " + str(self.dexterity) + "\n")

    def display_current_health(self):
        print(" CURRENT HEALTH: " + str(self.currhealth) + "\n")

    def display_current_luck(self):
        print(" CURRENT LUCK: " + str(self.currluck) + "\n")

    def display_inventory(self):
        print(" YOU HAVE: " + self.inventory[0] + ", " + self.inventory[1] + ", " + self.inventory[2])

    def print_character(self):
        print_skulls()
        self.display_name()
        self.display_current_stats()
        self.display_inventory()
        print_skulls()

    def print_character_in_fight(self):
        print_skulls()
        self.display_name()
        self.display_starting_health()
        self.display_current_health()
        self.display_dexterity()
        self.display_starting_luck()
        self.display_current_luck()
        print_skulls()

    def strike(self, opponent):
        roll_dice_for_self = randint(2, 12)
        roll_diece_for_opponent = randint(2, 12)
        own_dexterity = self.dexterity + roll_dice_for_self
        opponent_dexterity = opponent.dexterity + roll_diece_for_opponent
        if own_dexterity > opponent_dexterity:
            return "player hit"
            print("You hit " + opponent.name.upper() + "!")
        elif own_dexterity < opponent_dexterity:
            return "monster hit"
            print(opponent.name.upper() + " hit you!")
        else:
            return "draw"
            print("It's a draw!")

    def suffer_damage(self, damage):
        self.currhealth -= damage

    def try_luck(self):
        roll_dice = randint(2, 12)
        if self.currluck >= roll_dice:
            return "luck"
            self.currluck -= 1
            print("You are lucky!")
        else:
            return "no luck"
            print("No luck this time!")

    def save_character(self):
        player = {
            "NAME": self.name.upper(),
            "DEXTERITY": self.dexterity,
            "STARTING (MAX) HEALTH": self.maxhealth,
            "CURRENT HEALTH": self.currhealth,
            "STARTING (MAX) LUCK": self.maxluck,
            "LUCK": self.currluck,
            "INVENTORY": self.inventory
            }
        print(player)

class Monster(Player):
    def __init__(self = None,
        name = None,
        dexterity = None,
        maxhealth = None,
        currhealth = None,
        ):
        super().__init__(name, dexterity, maxhealth, currhealth)

    def print_monster_in_fight(self):
        print(" VS. ")
        print_skulls()
        self.display_name()
        self.display_starting_health()
        self.display_current_health()
        self.display_dexterity()
        print_skulls()
