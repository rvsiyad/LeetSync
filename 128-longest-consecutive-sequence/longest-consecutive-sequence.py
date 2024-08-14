class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxSequence = 0
        count = 1
    
        dictionary = {}

        for i in nums:
            dictionary[i] = 1 + dictionary.get(i, 0)
        
        for i in nums:
            if i - 1 not in dictionary:
                count = 1

                while (i + count) in dictionary:
                    count += 1
            maxSequence = max(maxSequence, count)
        
        return maxSequence