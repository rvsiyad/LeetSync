class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # First find the most frequent number
        count = {}

        for i in nums:
            count[i] = 1 + count.get(i, 0)
        
        mostFrequent = []

        topFrq = max(count.values())

        for key, value in count.items():
            if value == topFrq:
                mostFrequent.append(key)
        
        smallestSubArray = float("inf")
        
        # We need to find the smallest subarray we can get for all values in mostFrequent array
        while mostFrequent:
            value = mostFrequent.pop()
            valueFreq = count[value]
    
            currLength = 0

            L = 0
            R = len(nums) - 1

            while nums[L] != value:
                L += 1

            while nums[R] != value:
                R -= 1    
            
                
            currLength = R - L + 1
            
            smallestSubArray = min(smallestSubArray, currLength)

        return smallestSubArray