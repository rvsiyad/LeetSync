class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Take the count of each t character
        tCount = collections.defaultdict(int)
        sCount = collections.defaultdict(int)

        for char in t:
            tCount[char] += 1
        
        need = len(tCount)
        have = 0
        string = ""
        minLength = float("inf")

        L = 0

        for R in range(len(s)):
            sCount[s[R]] += 1

            if sCount[s[R]] == tCount[s[R]]:
                have += 1
            
            while have >= need:
                currentLength = R - L + 1
            
                if currentLength < minLength:
                    minLength = currentLength
                    string = s[L: R + 1]
                
                sCount[s[L]] -= 1

                if sCount[s[L]] < tCount[s[L]]:
                    have -= 1

                L += 1
        
        return string