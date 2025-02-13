class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Go in reverse and the the first none greater number than the previous
        # If pivot is still -1, reverse and return.
        pivot = -1 

        # Go backwards
        for i in range(len(nums) -1 , 0, -1):
            if nums[i] > nums[i - 1]:
                pivot = i - 1

                break
        
        # The array was constanly increasing from the right, then we have a number that needs to start over, smallest is it in reverse.
        if pivot == -1:
            nums.reverse()
            return
        
        # Now need to find the first greatest number from the end. We know the array is increasing in order from the right, so we can find one there.
        swap = len(nums) - 1

        while nums[swap] <= nums[pivot]:
            swap -= 1
        
        nums[swap], nums[pivot] = nums[pivot], nums[swap]

        # Everyything from pivot onwards needs to be reversed

        nums[pivot + 1:] = reversed(nums[pivot + 1:])
        return
        
