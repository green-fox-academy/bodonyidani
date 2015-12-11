import unittest
from names import CreateNames

class TestCreateNames(unittest.TestCase):
    def setUp(self):
        self.names = [{"id": 1, "name": "John"},
                      {"id": 2, "name": "Molly"},
                      {"id": 3, "name": "Jane"}]

    def test_instantiate(self):
        self.assertIsInstance(CreateNames([]), CreateNames)

    def test_names_as_list_when_empty(self):
        subject = CreateNames([])
        self.assertEqual(subject.names_as_list(), [])

    def test_names_as_list(self):
        subject = CreateNames(self.names)
        self.assertEqual(subject.names_as_list(), ["John", "Molly", "Jane"])

    def test_names_starting_with_j(self):
        subject = CreateNames(self.names)
        self.assertEqual(subject.names_starting_with_j(), ["John", "Jane"])

unittest.main()
