from display import print_skulls

class Player():
    def __init__(self = None, name = None, dexterity = None, health = None, luck = None, inventory = ["SWORD", "LEATHER ARMOR"]):
        self.name = name
        self.dexterity = dexterity
        self.health = health
        self.luck = luck
        self.inventory = inventory

    def set_name(self, name):
        self.name = name.upper()

    def set_initial_dexterity_health_luck(self, dexterity, health, luck):
        self.dexterity = dexterity
        self.health = health
        self.luck = luck

    def set_potion(self, potion):
        self.inventory = [self.inventory[0], self.inventory[1]]
        self.inventory.append(potion)

    def display_name(self):
        print(" NAME: " + str(self.name) + "\n")

    def display_stats(self):
        print(" DEXTERITY: " + str(self.dexterity) + "\n")
        print(" HEALTH: " + str(self.health) + "\n")
        print(" LUCK: " + str(self.luck) + "\n")

    def display_inventory(self):
        print(" YOU HAVE: " + self.inventory[0] + ", " + self.inventory[1] + ", " + self.inventory[2])

    def print_character(self):
        print_skulls()
        self.display_name()
        self.display_stats()
        self.display_inventory()
        print_skulls()
