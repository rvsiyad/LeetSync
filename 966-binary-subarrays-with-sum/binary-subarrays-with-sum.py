'''
We are given an array made of 1's and 0's, we are given a goal sum

We need to return num of subarrays which equal the goal sum

- We create a prefix sum, keeps the current counts at each index
- Then we can add the hashmap counts to a hashmap, we need to check if diff in hashmap, if so we add to result counts
'''
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum = [0] * (len(nums) + 1)
        prefix_map = {0: 1}
        result = 0

        for i in range(len(nums)):
            prefix_sum[i + 1] = prefix_sum[i] + 1 if nums[i] == 1 else prefix_sum[i]

            diff = prefix_sum[i + 1] - goal

            if diff in prefix_map:
                result += prefix_map[diff]
            
            prefix_map[prefix_sum[i + 1]] = 1 + prefix_map.get(prefix_sum[i + 1], 0)

        return result