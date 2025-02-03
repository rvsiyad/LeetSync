class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        
        print(self.longestSubarrayIncreasing(nums))
        print(self.longestSubarrayDecreasing(nums))

        return max(self.longestSubarrayIncreasing(nums), self.longestSubarrayDecreasing(nums))
    
    def longestSubarrayIncreasing(self, nums):
        maxLength = 0

        L = 0

        for R in range(1, len(nums)):
            if nums[R] <= nums[R - 1]:
                L = R  
            maxLength = max(maxLength, R - L + 1)
        
        return maxLength
    
    def longestSubarrayDecreasing(self, nums):
        maxLength = 0

        L = 0

        for R in range(1, len(nums)):
            if nums[R] >= nums[R - 1]:
                L = R  
            maxLength = max(maxLength, R - L + 1)
        
        return maxLength
                