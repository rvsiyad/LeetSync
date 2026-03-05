'''
We are given an array, we need to return the number of subarrays where the count of odd numbers equals k

We create a prefix where each index shows the number of odd numbers at each index

We can also create a hashmap, where current count - k is in the hashmap, if we move it and find the diff, then we know there is a count.

Each time we see a count we can increment it by one.
'''
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix_sum = [0] * (len(nums) + 1)
        prefix_map = {0: 1}

        result = 0

        for i, num in enumerate(nums):
            prefix_sum[i + 1] = prefix_sum[i] + 1 if num % 2 != 0 else prefix_sum[i]

            diff = prefix_sum[i + 1] - k
            if diff in prefix_map:
                result += prefix_map[diff] 

            prefix_map[prefix_sum[i + 1]] = 1 + prefix_map.get(prefix_sum[i + 1], 0)
        
        return result

        