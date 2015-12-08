import random

class Weapon:
    def strike(self, warrior, opponent):
        warrior.hp -= self.self_damage()
        opponent.hp -= self.damage()

    def damage(self):
        raise "Not implemented"

    def self_damage(self):
        raise "Not implemented"

class Sword(Weapon):
    def damage(self):
        return 10

    def self_damage(self):
        return 0

class Flamethrower(Weapon):
    def damage(self):
        return 50

    def self_damage(self):
        return 20

class CriticalSword(Weapon):
    def damage(self):
        return 10 + random.randint(0, 10)

    def self_damage(self):
        return 0

class Warrior:
    def __init__(self, weapon):
        self.weapon = weapon
        self.hp = 100

    def strike(self, opponent):
        self.weapon.strike(self, opponent)

    def __repr__(self):
        return "Warrior hp={}".format(self.hp)

warrior = Warrior(Sword())
monster = Warrior(Flamethrower())

warrior.strike(monster)
print(warrior)
print(monster)

class Enchanted(Weapon):
    def __init__(self, weapon):
        self.weapon = weapon

    def damage(self):
        return self.weapon.damage() * 2

    def self_damage(self):
        return self.weapon.self_damage() / 2

wizard = Warrior(Enchanted(Flamethrower()))
loser = Warrior(Sword())

wizard.strike(loser)
print(wizard)
print(loser)
