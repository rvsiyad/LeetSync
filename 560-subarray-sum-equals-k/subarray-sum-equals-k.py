class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # We can create a prefix sum using a hashmap, increase the count of that prefix sum occuring.
        # We create a prefix value, equal 0.
        # We go through each element in nums
        # Add prefix to the hashmap, increment count by 1
        # Check if currentSum - k in hashmap, if yes add count of diff to result

        """
        nums = [1,1,1]
        k = 2

        prefixSum = 0
        result = 0
        total = 1


        dict = {
            0: 1,

        }
        """
        result = 0
        total = 0

        prefix = {
            0: 1
        }

        for num in nums:
            total += num
            diff = total - k

            
            result += prefix.get(diff, 0)
            prefix[total] = 1 + prefix.get(total, 0)
    
        return result
