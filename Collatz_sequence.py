class Solution:
    def solve(self, n):
        a=1
        while n != 1:
            a=a+1
            print(n, end = ' ') 
            if n & 1: 
                n=3 * n + 1
            else: 
                n = n // 2
        
        return a