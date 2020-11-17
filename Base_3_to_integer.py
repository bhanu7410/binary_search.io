class Solution:
   def solve(self, s):
      ans = 0
      for c in s:
         ans = 3 * ans + int(c)
      return ans