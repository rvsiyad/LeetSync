class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = 0
        R = len(nums) - 1

        while L <= R:
            m = L + (R - L) // 2

            if m > 0 and nums[m] < nums[m - 1]:
                R = m - 1
            elif m < len(nums) - 1 and nums[m + 1] > nums[m]:
                L = m+1
            else:
                return m