import unittest
from sudoku_validator import *

class TestSudoku(unittest.TestCase):
    def test_empty_row(self):
        self.assertEqual(validate_row([]), False)

    def test_size_2(self):
        self.assertEqual(validate_row([1, 2]), True)

unittest.main()
