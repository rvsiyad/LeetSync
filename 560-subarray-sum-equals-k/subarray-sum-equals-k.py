class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefixCount = collections.defaultdict(int)
        prefixSum = res = 0

        prefixCount[0] = 1

        for num in nums:
            prefixSum += num

            res += prefixCount[prefixSum - k]

            prefixCount[prefixSum] += 1
        
        return res
