import unittest
import defmult
class CalcTest(unittest.TestCase):
  def test_area(self):
    self.assertEqual(defmult.mult(4, 2),8)
  def test_area(self):
    self.assertEqual(defmult.mult(-4, 6),-24)
  def test_area(self):
    self.assertEqual(defmult.mult(20, 200),4000)

if __name__ == '__main__':
  unittest.main()