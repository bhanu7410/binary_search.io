def solve(n):
    n=str(n)
    if len(n)<2:
        n="00"+n
    n=list(n[::-1])
    n.insert(2, ".")
    i=6
    while i<len(n):
        n.insert(i, ",")
        i=i+4
    str1=""
    for ele in n:  
            str1 += ele
    
    return str1[::-1]


import unittest

class TestFlattenList(unittest.TestCase):
   def test_01(self):
      self.assertEqual(solve(132),"1.32" )
   def test_02(self):
      self.assertEqual(solve(2), "0.02")
   def test_03(self):
      self.assertEqual(solve(15), '.15')
   def test_04(self):
      self.assertEqual(solve(100000000),"1,000,000.00")
   def test_05(self):
      self.assertEqual(solve(54813847798),"548,138,477.98")
   def test_06(self):
      self.assertEqual(solve(0),"0.00")

if __name__ == '__main__':
   unittest.main(verbosity=2)