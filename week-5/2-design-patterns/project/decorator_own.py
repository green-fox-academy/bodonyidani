from decorator import Warrior, Sword, Enhanced, Magical

class Wand:
    def damage(self):
        return 20

class Elfmade:
    def __init__(self, weapon):
        self.weapon = weapon

    def damage(self):
        return self.weapon.damage() * 3
