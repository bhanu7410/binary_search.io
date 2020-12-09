def solve( s):
    def solve(self, s):
        t=s[::-1]
        return t==s

import unittest

class TestFlattenList(unittest.TestCase):
   def test_01(self):
      self.assertEqual(solve("14341"), True)
   def test_02(self):
      self.assertEqual(solve("123456789"), False)
   def test_03(self):
      self.assertEqual(solve("racecar"), True)
   def test_04(self):
      self.assertEqual(solve("evilolive"),True)
   def test_05(self):
      self.assertEqual(solve("asfeasfd"), False)
   def test_06(self):
      self.assertEqual(solve("asphalt"),False)

if __name__ == '__main__':
   unittest.main(verbosity=2)