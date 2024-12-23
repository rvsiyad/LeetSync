class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = {}
        longest = 0

        L = 0

        for R in range(len(s)):
            unique[s[R]] = 1 + unique.get(s[R], 0)

            while max(unique.values()) > 1:
                unique[s[L]] -= 1

                if unique[s[L]] == 0:
                    del unique[s[L]]
                
                L += 1
            
            longest = max(longest, len(unique))
        
        return longest
            


