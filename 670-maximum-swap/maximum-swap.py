class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        nums = list(str(num))
        maxNum = "0"
        maxIndex = -1

        swap_i, swap_j = -1, -1

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > maxNum:
                maxNum = nums[i]
                maxIndex = i
            
            if nums[i] < maxNum:
                swap_i = i
                swap_j = maxIndex
        
        nums[swap_i], nums[swap_j] = nums[swap_j], nums[swap_i]

        return int("".join(nums))
 
