class Solution:
    def getSmallestString(self, s: str) -> str:
        minVal = s

        L = 0
        for R in range(1, len(s)):
            newS = list(s)
            leftVal, rightVal = int(newS[L]), int(newS[R])

            if (leftVal % 2 == 0 and rightVal % 2 == 0) or (leftVal % 2 != 0 and rightVal % 2 != 0):
                newS[L], newS[R] = newS[R], newS[L]

                newS = "".join(newS)

                if newS < minVal:
                    minVal = newS
            
            L += 1
        
        return str(minVal)

            