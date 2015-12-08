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

    def heal(self, hp):
        self.hp += hp

    def notify(self, type, healer):
        if type == "heal":
            healer.inflict_damage(50)

class Healer:
    def __init__(self):
        self.companions = []
        self.hp = 200

    def notify(self, type, warrior):
        if type == "damage":
            warrior.heal(10)
            for companion in self.companions:
                companion.notify("heal", self)

    def join(self, companion):
        self.companions.append(companion)

    def strike(self, opponent):
            opponent.inflict_damage(10)

    def inflict_damage(self, damage):
        self.hp -= damage

rabbit = Warrior()
wolf = Warrior()
shaman = Healer()

rabbit.join(shaman)
shaman.join(wolf)

wolf.strike(rabbit)
print(rabbit.hp)
print(shaman.hp)
