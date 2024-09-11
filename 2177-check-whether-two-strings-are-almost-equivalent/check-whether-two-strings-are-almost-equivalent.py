class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        freq = {}

        for i in range(len(word1)):
            freq[word1[i]] = 1 + freq.get(word1[i], 0)
            freq[word2[i]] = freq.get(word2[i], 0) - 1

        
        for i in freq.values():
            if abs(i) > 3:
                return False
        
        return True