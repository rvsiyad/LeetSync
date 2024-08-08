class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = []
        total = 0
        for i in nums:
            total += i
            prefix.append(total)
        
        return prefix