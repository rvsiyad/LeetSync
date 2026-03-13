'''
 - Return sum of 3 ints that are closest to target
 - We use a 3 sum technique, sort and then L and R points
 - We can probably use BS.
 - Keep track of running number with smallest abs difference to target

Example:
nums = [-1,2,1,-4] target = 1
sorted_nums = [-4, -1, 1, 2]

curr = -4


'''

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        smallest_abs = float("inf")
        result = 0

        nums.sort()

        for i in range(len(nums)):
            current = nums[i]

            L = i + 1
            R = len(nums) - 1

            while L < R:
                curr_result = current + nums[L] + nums[R]

                if abs(target - curr_result) < smallest_abs:
                    smallest_abs = abs(target - curr_result)
                    result = curr_result
                
                if curr_result < target:
                    L += 1
                else:
                    R -= 1

        return result

