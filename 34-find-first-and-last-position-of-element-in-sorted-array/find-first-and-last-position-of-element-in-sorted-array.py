class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        firstElement = self.firstElementBS(nums, target)
        lastElement = self.lastElementBS(nums, target)

        return [firstElement, lastElement]
    
    def firstElementBS(self, nums, target):
        L = 0
        R = len(nums) - 1

        index = -1

        while L <= R:
            m = L + (R - L) // 2

            if nums[m] == target:
                index = m
                R = m - 1
                
            elif nums[m] > target:
                R = m - 1
            else:
                L = m + 1
        
        return index


    def lastElementBS(self, nums, target):
        L = 0
        R = len(nums) - 1

        index = -1

        while L <= R:
            m = L + (R - L) // 2

            if nums[m] == target:
                index = m
                L = m + 1
            elif nums[m] > target:
                R = m - 1
            else:
                L = m + 1
        
        return index