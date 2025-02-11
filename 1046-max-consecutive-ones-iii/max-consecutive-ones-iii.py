class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # Sliding window
        """
        We want to add to the sliding window will the number of zeros in the string is < k
        Since the numbers are 0 and 1, we can keep the count using an array, where the index represents the number
        We add to the right and remove from the left
        Use a while loop to keep removing from the L
        Use a two pointer to remove from L
        """
        count = [0, 0]
        L = 0
        maxLength = float("-inf")
        
        for R in range(len(nums)):
            # Increment num count by 1
            count[nums[R]] += 1

            while count[0] > k:
                # Remove elements from the left
                count[nums[L]] -= 1
                L += 1
            
            maxLength = max(maxLength, R - L + 1)
        
        return 0 if maxLength == float("-inf") else maxLength

