import unittest
from game import Menu, MenuItem

class TestMenu(unittest.TestCase):
    def test_choose(self):
        menu = Menu("TestMenuName",
            [MenuItem("S", "Test", lambda : True)],
            "TestInputPrompt")
        self.assertEqual(menu.choose("S"), True)

unittest.main()
