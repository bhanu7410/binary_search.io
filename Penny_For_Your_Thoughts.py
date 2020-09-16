class Solution:
    def solve(self, n):
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