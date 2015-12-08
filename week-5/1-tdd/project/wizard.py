from character import Character

class Wizard(Character):
    def __init__(self, name, hp, damage, manna):
        super().__init__(name, hp, damage)
        self.manna = manna

    def strike(self, opponent):
        if self.manna >= 5:
            opponent.hp -= self.damage * 3
            self.manna -= 5
        else:
            opponent.hp -= self.damage / 3
