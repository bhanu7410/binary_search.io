def solve( nums):
    l= sorted(nums)
    count = 0
    for i in range(len(nums)):
        if l[i]==nums[i]:
            count+=1
    return count

import unittest

class TestFlattenList(unittest.TestCase):
    def test_01(self):
        self.assertEqual(solve([12,13,54,8,79,87,9,7,8,7469,4,6,1,32]), 1)
    def test_02(self):
      self.assertEqual(solve([1, 7, 3, 4, 10]), 2)
    def test_03(self):
      self.assertEqual(solve([1,6,165,84,562,6,1625,165,]), 3)
    def test_04(self):
      self.assertEqual(solve([42,86,854,3648,368,361,23,41,812,48,94,236]),0)
    def test_05(self):
      self.assertEqual(solve([]), 0)
    def test_06(self):
      self.assertEqual(solve([1,2,3,4,89,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,5]),55)


if __name__ == '__main__':
    unittest.main(verbosity=2)