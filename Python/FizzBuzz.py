class Solution:
    def solve(self, n):
        
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