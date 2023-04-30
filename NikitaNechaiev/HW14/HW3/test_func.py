import unittest
import functions_with_errors

class TestTest(unittest.TestCase):
    def test_one(self):
        self.assertTrue(functions_with_errors.greeting_by_name('John'))
    def test_two(self):
        self.assertTrue(functions_with_errors.get_symbol_position('Hello john!','l'))
    def test_three(self):
        self.assertTrue(functions_with_errors.merge({'one , two'},{'three'}))
if __name__ == '__main__':
    unittest.main()