import unittest
import hw_14_practical_task_3 as file


class TestFunctionAreaRectangle(unittest.TestCase):
    def test_get_area_rectangle(self):
        self.assertEqual(file.get_area_rectangle(4, 6),
                         "S = 24 square units.",
                         "Test get_area_rectangle(length, width) is Failed")
        self.assertEqual(file.get_area_rectangle(3.6, 5.8),
                         "S = 20.88 square units.",
                         "Test get_area_rectangle(length, width) is Failed")
        self.assertEqual(file.get_area_rectangle(-4, 6),
                         "Length and width of rectangle must be non-negative numbers!",
                         "Test get_area_rectangle(length, width) is Failed")
        self.assertEqual(file.get_area_rectangle(0, -6),
                         "Length and width of rectangle must be non-negative numbers!",
                         "Test get_area_rectangle(length, width) is Failed")
        with self.assertRaises(TypeError, msg="Length and width of rectangle must be float type"):
            file.get_area_rectangle("6", 5)
            file.get_area_rectangle(6, "f")
            file.get_area_rectangle("9", "f")


if __name__ == "__main__":
    unittest.main()
