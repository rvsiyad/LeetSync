class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        currentSet = []
        nums.sort()

        def backtrack(index, currentSet):
            if index >= len(nums):
                subsets.append(currentSet.copy())
                return

            currentSet.append(nums[index])
            backtrack(index + 1, currentSet)

            # skip, but we want to skip those before aswell
            currentSet.pop()
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
            
            backtrack(index + 1, currentSet)
        
        backtrack(0, currentSet)
        return subsets
            
