class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = [0] * (len(nums) + 1)
        result = 0
        prefix_map = {0: 1}

        for i in range(len(nums)):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

            if prefix_sum[i + 1] - k in prefix_map:
                result += prefix_map[prefix_sum[i + 1] - k]
        
            prefix_map[prefix_sum[i + 1]] = 1 + prefix_map.get(prefix_sum[i + 1], 0)

        # Now we need to go through hashmap and see depending on counts of values seen
        
        return result
