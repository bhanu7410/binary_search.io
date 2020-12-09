def solve( n):
    
    fb = []
    
    for i in range(1, n+1):
        
        if (i % 3 == 0) and (i % 5 != 0):
            f = "Fizz"
        elif (i % 3 != 0) and (i % 5 == 0):
            f = "Buzz"
        elif (i % 3 == 0) and (i % 5 == 0):
            f = "FizzBuzz"
        else:
            f = str(i)
            
        fb.append(f)
        
    return fb

import unittest

class TestFlattenList(unittest.TestCase):
    def test_01(self):
        self.assertEqual(solve(5), ["1","2","Fizz","4","Buzz"])
    def test_02(self):
        self.assertEqual(solve(1), ["1"])
    def test_03(self):
        self.assertEqual(solve(15), ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"])
    def test_04(self):
        self.assertEqual(solve(7), ["1","2","Fizz","4","Buzz","Fizz","7"])
    def test_05(self):
        self.assertEqual(solve(0), [])
    def test_06(self):
        self.assertEqual(solve(10), ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz"])
if __name__ == '__main__':
    unittest.main(verbosity=2)