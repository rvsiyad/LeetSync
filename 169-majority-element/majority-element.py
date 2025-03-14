class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)

        for key, value in counter.items():
            if value >= len(nums) / 2:
                return key