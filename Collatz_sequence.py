def solve(n):
    a=1
    while n != 1:
        a=a+1
        if n & 1: 
            n=3 * n + 1
        else: 
            n = n // 2
    
    return a

import unittest

class TestFlattenList(unittest.TestCase):
    def test_01(self):
        self.assertEqual(solve(11), 15)
    def test_02(self):
        self.assertEqual(solve(1), 1)
    def test_03(self):
        self.assertEqual(solve(156), 37)
    def test_04(self):
        self.assertEqual(solve(374829),180)
    def test_05(self):
        self.assertEqual(solve(12), 10)
    def test_06(self):
        self.assertEqual(solve(658730),62)

if __name__ == '__main__':
    unittest.main(verbosity=2)
                