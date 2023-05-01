import unittest
import functions as f


class FunctionTest(unittest.TestCase):
    def test_greeting_by_name(self):
        self.assertEqual(f.greeting_by_name("World"), "Hello World!",
                         "Test greeting_by_name(name) is Failed")

    def test_get_symbol_position(self):
        self.assertEqual(f.get_symbol_position("Python", "P"), 1,
                         "Test get_symbol_position(text, symbol) with success is Failed")
        self.assertEqual(f.get_symbol_position("Python", "Py"), "Error! Symbol can be string with only one letter",
                         "Test get_symbol_position(text, symbol) when symbol incorrect is Failed")
        self.assertEqual(f.get_symbol_position("Python", "a"), "Not found",
                         "Test get_symbol_position(text, symbol) when symbol was not found is Failed")

    def test_merge(self):
        self.assertEqual(f.merge({1: "one"}, {2: "two"}), {1: "one", 2: "two"},
                         "Test merge(dict1, dict2) is Failed")
        with self.assertRaises(TypeError, msg="Test merge(dict1, dict2) dict1 immutability is Failed"):
            f.merge({[1]: 6}, {3: "three"})
        with self.assertRaises(TypeError, msg="Test merge(dict1, dict2) dict2 immutability is Failed"):
            f.merge({1: 6}, {[3]: "three"})


if __name__ == "__main__":
    unittest.main()
