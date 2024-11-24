class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        tCount, sCount = {}, {}

        for c in t:
            tCount[c] = 1 + tCount.get(c, 0)
        
        res, minLength, have, need = [-1, -1], float("inf"), 0, len(tCount)

        L = 0

        for R in range(len(s)):
            sCount[s[R]] = 1 + sCount.get(s[R], 0)

            if s[R] in tCount and sCount[s[R]] == tCount[s[R]]:
                have += 1
            
            while have == need:
                if (R - L + 1) < minLength:
                    res = [L, R]
                    minLength = (R - L + 1)

                sCount[s[L]] -= 1

                if s[L] in tCount and sCount[s[L]] < tCount[s[L]]:
                    have -= 1
                
                L += 1
        
        start, end = res

        return s[start:end+ 1] if minLength != float("inf") else ""