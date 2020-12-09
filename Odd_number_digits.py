def solve(nums):
    a=0
    for i in nums:
        if len(str(i))%2==1:
            a=a+1
    
    return a

import unittest

class TestFlattenList(unittest.TestCase):
   def test_01(self):
      self.assertEqual(solve([1, 800, 2, 10, 3]), 4)
   def test_02(self):
      self.assertEqual(solve([1,123,352123,673342,598234]), 2)
   def test_03(self):
      self.assertEqual(solve([91,984,9684,1,919,814,18974,161,984,16,19874,965,41]), 9)
   def test_04(self):
      self.assertEqual(solve([19,1,961,9619,419,49621,91,52641,9198,496,14,219,846,298,462,941,641,891,6549,219,496,14894]),16)
   def test_05(self):
      self.assertEqual(solve([4891,89140,849,2,409,4384365187,13,8743,654,384,84,354,53,43,436,48,6436,4,34,3684,34,634,368,46,436,4683,436,478635,4]), 14)
   def test_06(self):
      self.assertEqual(solve([84,984,99,494,94,51,324,6413,874,4187,43,4568436,576,341367,43645,384,374,313,643,368,35,43641]),13)

if __name__ == '__main__':
   unittest.main(verbosity=2)