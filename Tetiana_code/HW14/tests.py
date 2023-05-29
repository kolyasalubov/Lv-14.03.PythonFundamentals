import unittest
from functions import greeting_by_name, get_symbol_position, merge
#from functions_with_errors import greeting_by_name, get_symbol_position, merge


class TestFunctions(unittest.TestCase):
    def test_greeting_by_name(self):
        self.assertEqual(greeting_by_name("Alice"),
                         "Hello Alice!",
                         "Test for valid inputs failed!")
        self.assertEqual(greeting_by_name("Bob"),
                         "Hello Bob!",
                         "Test for valid inputs failed!")
        self.assertEqual(greeting_by_name(""),
                         "Hello !",
                         "Test for empty inputs failed!")
        
    def test_get_symbol_position(self):
        self.assertEqual(get_symbol_position("SuperMax", "a"),
                         7,
                         "Test for valid inputs failed!")
        self.assertEqual(get_symbol_position("Hello, world!", ","),
                         6,
                         "Test for valid inputs failed!")
        self.assertEqual(get_symbol_position("Python", "x"),
                         "Not found",
                         "Test for missing symbol failed!")

    def test_merge(self):
        self.assertEqual(merge({1 : "A"}, {2 : "B"}),
                         {1 : "A", 2 : "B"},
                         "Test for simple inputs failed!")
        self.assertEqual(merge({}, {}),
                         {},
                         "Test for empty inputs failed!")
        self.assertEqual(merge({"A" : "A"}, {3.0 : 5}),
                         {"A" : "A", 3.0 : 5},
                         "Test for different inputs failed")
        dict1 = {1 : "A"}
        dictc1 = {1 : "A"}
        dict2 = {2 : "B"}
        dictc2 = {2 : "B"}
        result = {1 : "A", 2 : "B"}
        self.assertEqual(merge(dict1, dict2),
                         result,
                         "Mutability test fail!")
        self.assertEqual(dict1, dictc1,"Mutability test fails!")
        self.assertEqual(dict2, dictc2,"Mutability test fails!")

if __name__ == "__main__":
    unittest.main()
