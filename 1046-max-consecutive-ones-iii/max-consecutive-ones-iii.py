class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count = {}
        maxLength = float("-inf")

        L = 0

        for R in range(len(nums)):
            count[nums[R]] = 1 + count.get(nums[R], 0)

            while count.get(0, 0) > k:
                count[nums[L]] -= 1
                L += 1
            
            maxLength = max(maxLength, R - L + 1)
        
        return maxLength
            


