# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
import random
class Solution:
    def __init__(self, w: List[int]):
        # Create a prefix sum, check if num is 
        self.prefix = []

        cur = 0

        for weight in w:
            cur += weight
            self.prefix.append(cur)

        self.total = cur

    def pickIndex(self) -> int:
        target = random.uniform(0, self.total)

        L = 0
        R = len(self.prefix)

        while L < R:
            m = (L + R)//2

            if target > self.prefix[m]:
                L = m + 1
            else:
                R = m

        return L
        


