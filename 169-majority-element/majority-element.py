class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maxCount = 0
        maxValue = 0
        counter = {}

        for num in nums:
            counter[num] = counter.get(num, 0) + 1

            if counter[num] > maxCount:
                maxCount = counter[num]
                maxValue = num
        
        return maxValue