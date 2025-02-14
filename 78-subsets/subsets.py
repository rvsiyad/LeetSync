class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def backtrack(i, arr):
            if i >= len(nums):
                res.append(arr[:])
                return
            
            arr.append(nums[i])
            backtrack(i + 1, arr)

            arr.pop()
            backtrack(i + 1, arr)
        
        backtrack(0, [])

        return res