class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # Use binary search, check if we are in a montoinc increasing or decreasing array
        L = 0
        R = len(nums) - 1

        while L <= R:
            m = (L + R) // 2

            if m > 0 and nums[m] < nums[m - 1]:
                R = m - 1
            elif m < len(nums) - 1 and nums[m] < nums[m + 1]:
                L = m + 1
            else:
                return m