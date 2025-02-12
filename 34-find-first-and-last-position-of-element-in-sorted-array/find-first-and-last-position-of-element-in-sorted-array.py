class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Binary search
        # Two pass? Once to find the left start and one to find the right start
        L = 0
        R = len(nums) - 1

        # Find the target and then we can search while loop to find the left most and right most occurences?
        
        startIndex = self.findFirstElement(nums, target)
        endIndex = self.findLastElement(nums, target)
            
        return [startIndex, endIndex]

    def findFirstElement(self, nums, target):
        L = 0
        R = len(nums) - 1

        while L <= R:
            m = (L + R) // 2

            if nums[m] == target:
                if m == 0 or nums[m] != nums[m - 1]:
                    return m
                else:
                    R = m - 1
            elif nums[m] > target:
                R = m - 1
            else:
                L = m + 1
        
        return -1
            
    def findLastElement(self, nums, target):
        L = 0
        R = len(nums) - 1

        while L <= R:
            m = (L + R) // 2

            if nums[m] == target:
                if m == len(nums) - 1 or nums[m] != nums[m + 1]:
                    return m
                else:
                    L = m + 1
            elif nums[m] > target:
                R = m - 1
            else:
                L = m + 1
        
        return -1