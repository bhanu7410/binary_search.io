def solve(text, word0, word1):
    words = text.split(' ')
    
    last_w0 = -1
    last_w1 = -1
    dist = -1
    
    for w, word in enumerate(words):
        if word == word0:
            if last_w1 != -1 and (dist == -1 or dist > w - last_w1):
                dist = w - last_w1 - 1
                if dist == 0:
                    return 0
            last_w0 = w
        if word == word1:
            if last_w0 != -1 and (dist == -1 or dist > w - last_w0):
                dist = w - last_w0 - 1
                if dist == 0:
                    return 0
            last_w1 = w
                    
    if last_w0 == -1 or last_w1 == -1:
        return -1
        
    else:
        return dist


import unittest

class TestFlattenList(unittest.TestCase):

    def test_01(self):
        self.assertEqual(solve("dog cat hello cat dog dog hello cat world","hello","world"), 1)

    def test_02(self):
        self.assertEqual(solve("","",""), -1)

    def test_03(self):
        self.assertEqual(solve("","hey","heuh"), -1)

    def test_04(self):
        self.assertEqual(solve("dog cat hello cat dog dog hello cat world","dog","cat"),0)

    def test_05(self):
        self.assertEqual(solve("Peter Piper picked Piper a peck of picked a a Piper","picked","Piper"), 0)

    def test_06(self):
        self.assertEqual(solve("wood would a wood a c chuck chuck if a woodchuck could chuck wood","would","chuck"),4 )

if __name__ == '__main__':
    unittest.main(verbosity=2)
