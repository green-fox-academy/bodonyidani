class GameCharacter:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def print_status(self):
        if self.hp <= 0:
            print(self.name + " is kaput.")
        else:
            print(self.name + " has " + str(self.hp) + " HP " + "and " + str(self.damage) + " damage.")

    def drink_potion(self):
        if self.hp <= 0:
            print("Too little, too late.")
        else:
            self.hp += 10

    def strike(self, other):
        if self.hp <= 0:
            print("Zombies cannot strike.")
        elif other.hp <= 0:
            print("You cannot strike a zombie.")
        else:
            other.hp -= self.damage

class Cerlic(GameCharacter):
    def heal(self, ally):
        ally.hp += 10

Wizard = GameCharacter("Wizard", 10, 5)
Ogre = GameCharacter("Ogre", 5, 1)
Melkor = Cerlic("Melkor", 100, 8)
