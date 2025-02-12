class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Binary search
        # Two pass? Once to find the left start and one to find the right start
        L = 0
        R = len(nums) - 1

        # Find the target and then we can search while loop to find the left most and right most occurences?
        def binarySearch(nums, target, leftBias):
            L = 0
            R = len(nums) - 1

            i = -1

            while L <= R:
                m = (L + R) // 2

                if nums[m] > target:
                    R = m - 1
                elif nums[m] < target:
                    L = m + 1
                else:
                    i = m
                    if leftBias:
                        R = m - 1
                    else:
                        L = m + 1

            return i
        
        start = binarySearch(nums, target, True)
        end = binarySearch(nums, target, False)
            
        return [start, end]


