import random

class Solution(object):

    def __init__(self, w):
        self.prefix = []

        total = 0
        for num in w:
            total += num
            self.prefix.append(total)

    def pickIndex(self):
        target = random.uniform(0, self.prefix[-1])
        
        L = 0
        R = len(self.prefix)

        while L < R:
            m = L + (R - L) // 2

            if self.prefix[m] < target:
                L = m + 1
            else:
                R = m
        
        return L



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()