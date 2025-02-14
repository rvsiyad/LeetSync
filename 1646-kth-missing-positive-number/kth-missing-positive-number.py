class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        missingNumbers = []

        arrPointer = 0
        i = 1

        while len(missingNumbers) < k and arrPointer < len(arr):
            if arr[arrPointer] != i:
                missingNumbers.append(i)
            else:
                arrPointer += 1
            
            i += 1
        
        while len(missingNumbers) < k:
            missingNumbers.append(i)
            i += 1
        
        
        return missingNumbers[-1]