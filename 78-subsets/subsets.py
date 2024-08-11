class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def helper(index):
            if index >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[index])
            helper(index + 1)

            subset.pop()
            helper(index + 1)
        
        helper(0)
        return res