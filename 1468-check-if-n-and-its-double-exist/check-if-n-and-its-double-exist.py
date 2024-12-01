class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        numSet = set()

        for i in range(len(arr)):
            if (arr[i] * 2) in numSet:
                return True
            elif (arr[i] / 2) in numSet:
                return True
            else:
                numSet.add(arr[i])
        
        return False