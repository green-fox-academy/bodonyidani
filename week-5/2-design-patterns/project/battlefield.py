class Warrior:
    def __init__(self):
        self.companions = []
        self.hp = 100

    def join(self, companion):
        self.companions.append(companion)

    def strike(self, opponent):
        opponent.inflict_damage(10)

    def inflict_damage(self, damage):
        self.hp -= damage
        for companion in self.companions:
            companion.notify("damage", self)

class Battlefield:
    def notify(self, type, warrior):
        if type == "damage":
            self.strike(warrior)

    def strike(self, warrior):
            warrior.hp -= 10

rabbit = Warrior()
fox = Warrior()
battlefield = Battlefield()
fox.join(battlefield)
rabbit.join(battlefield)

fox.strike(rabbit)

print(fox.hp)
print(rabbit.hp)
