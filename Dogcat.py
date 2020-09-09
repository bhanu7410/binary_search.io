class Solution:
    def solve(self, text, word0, word1):
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
                