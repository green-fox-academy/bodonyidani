import unittest
from katapotter import *

class TestPotter(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(discounter([]), 0)

    def test_one_book(self):
        self.assertEqual(discounter([1]), 8)

    def test_two_consecutive_books(self):
        self.assertEqual(discounter([1, 2]), 2 * 8 * 0.95)

    def test_three_consecutive_books(self):
        self.assertEqual(discounter([1, 2, 3]), 3 * 8 * 0.9)

    def test_four_consecutive_books(self):
        self.assertEqual(discounter([1, 2, 3, 4]), 4 * 8 * 0.8)

    def test_five_consecutive_books(self):
        self.assertEqual(discounter([1, 2, 3, 4, 5]), 5 * 8 * 0.75)

    def test_two_identical_books(self):
        self.assertEqual(discounter([2, 2]), 2 * 8)

    def test_three_books_two_different(self):
        self.assertEqual(discounter([1, 2, 1]), 8 + 2 * 8 * 0.95)

    def test_five_books_three_different(self):
        self.assertEqual(discounter([1, 2, 2, 3, 3]), 8 * (3 * 0.9 + 2 * 0.95))

unittest.main()
