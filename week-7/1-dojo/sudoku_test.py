import unittest
from sudoku import *

class TestArrayValidator(unittest.TestCase):
    def test_validator_existance(self):
        self.assertEqual(validate_array([]), False)

    def test_validator_has_invalid_input(self):
        self.assertEqual(validate_array([1, 2]), False)

    def test_9_length_array(self):
        self.assertEqual(validate_array([1, 2, 3, 4, 5, 6, 7, 8, 9]), True)

    def test_if_number(self):
        self.assertEqual(validate_array([2, "a", 3, 5, 7, 4, 2, 1, 9]), False)

    def test_unordered_numbers(self):
        self.assertEqual(validate_array([1, 2, 4, 3, 5, 6, 7, 8, 9]), True)

    def test_4_length_array(self):
        self.assertEqual(validate_array([1, 2, 3, 4]), True)

    def test_16_length_array(self):
        self.assertEqual(validate_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]), True)

unittest.main()
