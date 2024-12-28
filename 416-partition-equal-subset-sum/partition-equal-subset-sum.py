class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # We need to check if the currentSum and the newArray sum are equal.
        # We can do this by checking if adding the current value at nums is possible to split evenly or not
        # Our base case is checking if the index is out of bounds.
        # Take/skip approach, we can add caching after getting the recursive approach.
        numsTotal = sum(nums)

        if numsTotal % 2 != 0:
            return False

        targetValue = numsTotal // 2

        def memoization(i, currentSum, targetValue, cache):
            if i >= len(nums):
                return False
            
            if (currentSum) == (targetValue):
                return True
            
            if (i, currentSum) in cache:
                return cache[(i, currentSum)]

            # Skip. what do we do? Return if we have a path or not?
            skipValue = memoization(i + 1, currentSum, targetValue, cache)

            # Taking the value?
            takeValue = memoization(i + 1, currentSum + nums[i], targetValue, cache)

            cache[(i, currentSum)] = skipValue or takeValue
        
            return cache[(i, currentSum)]
        
        return memoization(0, 0, targetValue, {})