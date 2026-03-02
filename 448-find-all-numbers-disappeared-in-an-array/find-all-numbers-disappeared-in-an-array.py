class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        num_seen = [False for _ in range(len(nums))]

        for num in nums:
            num_seen[num - 1] = True
        
        result = []

        for i in range(1, len(nums) + 1):
            if num_seen[i - 1] == False:
                result.append(i)
        
        return result