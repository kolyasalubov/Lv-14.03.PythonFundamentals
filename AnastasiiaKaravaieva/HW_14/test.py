import unittest
from functions import greeting_by_name, get_symbol_position, merge
from functions_with_errors import greeting_by_name, get_symbol_position, merge


class FunctionsTest(unittest.TestCase):
    def test_greeting_by_name(self):
        name = "John"
        expected_result = "Hello John!"
        self.assertEqual(greeting_by_name(name), expected_result)

        name = ""
        expected_result = "Hello !"
        self.assertEqual(greeting_by_name(name), expected_result)

        name = "   "
        expected_result = "Hello    !"
        self.assertEqual(greeting_by_name(name), expected_result)

    def test_get_symbol_position(self):

        self.assertEqual(get_symbol_position("Hello", "e"), 2)

        self.assertEqual(get_symbol_position("Hello", "n"), "Not found")

        self.assertEqual(get_symbol_position("Hello", "ell"),
                         "Error! Symbol can be string with only one letter")

    def test_merge(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'c': 3, 'd': 4}
        expected_result = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        self.assertEqual(merge(dict1, dict2), expected_result)

        dict1 = {}
        dict2 = {'a': 1, 'b': 2}
        expected_result = {'a': 1, 'b': 2}
        self.assertEqual(merge(dict1, dict2), expected_result)

        dict1 = {'a': 1, 'b': 2}
        dict2 = {}
        expected_result = {'a': 1, 'b': 2}
        self.assertEqual(merge(dict1, dict2), expected_result)

        dict1 = {}
        dict2 = {}
        expected_result = {}
        self.assertEqual(merge(dict1, dict2), expected_result)


if __name__ == '__main__':
    unittest.main()