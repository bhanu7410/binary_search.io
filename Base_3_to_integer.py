def solve(s):
   ans = 0
   for c in s:
      ans = 3 * ans + int(c)
   return ans

import unittest

class TestFlattenList(unittest.TestCase):
   def test_01(self):
      self.assertEqual(solve("11"), 4)
   def test_02(self):
      self.assertEqual(solve("1"), 1)
   def test_03(self):
      self.assertEqual(solve("156"), 30)
   def test_04(self):
      self.assertEqual(solve("374829"),1491)
   def test_05(self):
      self.assertEqual(solve("12"), 5)
   def test_06(self):
      self.assertEqual(solve("658730"),2151)

if __name__ == '__main__':
   unittest.main(verbosity=2)