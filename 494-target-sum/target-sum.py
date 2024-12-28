class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # We need to create the recurisve approach first and then add caching after
        # We want to calculate the number of ways we can create the target
        # We have to use all integers in the array.
        # We can only check if equals target once the index is out of bounds?
        def memoization(i, currentSum, cache):
            if i >= len(nums):
                if currentSum == target:
                    return 1
                else:
                    return 0
            
            if (i, currentSum) in cache:
                return cache[(i, currentSum)]
            
            plus = memoization(i + 1, currentSum + (+nums[i]), cache)

            minus = memoization(i + 1, currentSum + (-nums[i]), cache)

            cache[(i, currentSum)] = plus + minus

            return cache[(i, currentSum)]
        
        return memoization(0, 0, {})