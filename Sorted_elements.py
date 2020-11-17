class Solution:
    def solve(self, nums):
        l= sorted(nums)
        count = 0
        for i in range(len(nums)):
            if l[i]==nums[i]:
                count+=1
        return count