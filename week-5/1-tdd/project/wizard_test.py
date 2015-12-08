import unittest
from wizard import Wizard

class TestWizard(unittest.TestCase):
    def test_existence(self):
        wizard = Wizard("Merlin", 40, 10, 20)

    def test_inheritence(self):
        wizard = Wizard("Merlin", 40, 10, 20)
        self.assertEqual(wizard.hp, 40)

    def test_manna(self):
        wizard = Wizard("Merlin", 40, 10, 20)
        self.assertEqual(wizard.manna, 20)

    def test_strike_highmanna(self):
        wizard = Wizard("Merlin", 40, 10, 20)
        opponent = Wizard("Saruman", 50, 9, 4)
        wizard.strike(opponent)
        self.assertEqual(opponent.hp, 20)
        self.assertEqual(wizard.manna, 15)

    def test_strike_lowmanna(self):
        wizard = Wizard("Merlin", 40, 10, 20)
        opponent = Wizard("Saruman", 50, 9, 4)
        opponent.strike(wizard)
        self.assertEqual(wizard.hp, 37)
        self.assertEqual(opponent.manna, 4)

unittest.main()
