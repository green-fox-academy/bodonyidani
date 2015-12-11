import unittest
from duplicate_encoder import EncodeString

class TestEncodeString(unittest.TestCase):
    def setUp(self):
        string = EncodeString("test")

    def test_encoder(self):
        self.assertEqual(EncodeString("din").encode(), "(((")
        self.assertEqual(EncodeString("recede").encode(), "()()()")

unittest.main()
