class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return max(nums[0], 0)      
        
        arrWithFirstHouse = nums[:-1]
        arrWithoutFirstHouse = nums[1:]

        def calculateMaxSum(nums):
            prevHouse, curHouse = 0, 0

            for num in nums:
                temp = max(prevHouse + num, curHouse)
                prevHouse = curHouse
                curHouse = temp
            
            return curHouse
        
        return max(calculateMaxSum(arrWithFirstHouse), calculateMaxSum(arrWithoutFirstHouse))
