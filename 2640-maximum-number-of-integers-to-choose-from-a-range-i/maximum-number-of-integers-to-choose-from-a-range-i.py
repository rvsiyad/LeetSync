class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        bannedSet = set(banned)
        curSum = 0
        resultArr = []

        for i in range(1, n + 1):
            if i in bannedSet:
                continue
            
            if (curSum + i) > maxSum:
                return len(resultArr)
            else:
                curSum += i
                resultArr.append(i)
        
        return len(resultArr)
