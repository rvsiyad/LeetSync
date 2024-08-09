class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subTree = []

        def helper(index):
            if index >= len(nums):
                res.append(subTree.copy())
                return
            
            subTree.append(nums[index])
            helper(index + 1)

            subTree.pop()
            helper(index + 1)
        
        helper(0)
        return res