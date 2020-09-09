class Solution:
    def solve(self, nums):
        a=0
        for i in nums:
            if len(str(i))%2==1:
                a=a+1
        
        return a
