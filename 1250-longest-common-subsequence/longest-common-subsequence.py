class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        def dfs(text1Pointer, text2Pointer, text1, text2, cache):
            if text1Pointer >= len(text1) or text2Pointer >= len(text2):
                return 0
            
            # I dont think we should return if the pointers do not match, as we can still find a subsequence.
            # If the pointers do match, we want to move it along in the process and not check for the same sequence again?
            if (text1Pointer, text2Pointer) in cache:
                return cache[(text1Pointer, text2Pointer)]

            if text1[text1Pointer] == text2[text2Pointer]:
                cache[(text1Pointer, text2Pointer)] = 1 + dfs(text1Pointer + 1, text2Pointer + 1, text1, text2, cache)
                
            else:
                cache[(text1Pointer, text2Pointer)] = max(dfs(text1Pointer + 1, text2Pointer, text1, text2, cache), dfs(text1Pointer, text2Pointer + 1, text1, text2, cache))
            
            return cache[(text1Pointer, text2Pointer)]
        
        return dfs(0, 0, text1, text2, {})

            