class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1P, word2P = 0, 0

        newWord = ""

        while word1P < len(word1) and word2P < len(word2):
            newWord += word1[word1P]
            newWord += word2[word2P]

            word1P += 1
            word2P += 1
        
        while word1P < len(word1):
            newWord += word1[word1P]
            word1P += 1

        while word2P < len(word2):
            newWord += word2[word2P]
            word2P += 1
        
        return newWord