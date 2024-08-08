class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = {}
        maxVal = float("-inf")

        for i in arr:
            count[i] = 1 + count.get(i, 0)
        
        for key, value in count.items():
            if key == value:
                maxVal = max(maxVal, value)
        
        return -1 if maxVal == float("-inf") else maxVal

