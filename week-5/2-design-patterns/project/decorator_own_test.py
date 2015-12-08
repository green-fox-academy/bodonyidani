import unittest
from decorator_own import Warrior, Sword, Enhanced, Magical, Wand, Elfmade

class TestAdditionalPlayers(unittest.TestCase):
    def test_inheritence(self):
        warrior = Warrior(Enhanced(Sword()))
        opponent = Warrior(Sword())
        warrior.strike(opponent)
        self.assertEqual(opponent.hp, 85)

    def test_wand(self):
        warrior = Warrior(Wand())
        opponent = Warrior(Wand())
        warrior.strike(opponent)
        self.assertEqual(opponent.hp, 80)

    def test_elfmade(self):
        warrior = Warrior(Elfmade(Sword()))
        opponent = Warrior(Elfmade(Wand()))
        warrior.strike(opponent)
        opponent.strike(warrior)
        self.assertEqual(opponent.hp, 70)
        self.assertEqual(warrior.hp, 40)

if __name__ == "__main__":
    unittest.main()
