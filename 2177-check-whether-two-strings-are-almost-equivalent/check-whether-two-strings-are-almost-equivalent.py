class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        # Create two hashmaps/dicts
        # These will hold the letters as values
        # Go over both in one loop,
        # Add key and count the occurences

        word1Dic, word2Dic = {}, {}

        for i in range(len(word1)):
            word1Dic[word1[i]] = 1 + word1Dic.get(word1[i], 0)
            word2Dic[word2[i]] = 1 + word2Dic.get(word2[i], 0)

        for key, value in word1Dic.items():
            if key not in word2Dic:
                if value > 3:
                    return False
            elif abs(value - word2Dic[key]) > 3:
                return False
        
        for key, value in word2Dic.items():
            if key not in word1Dic:
                if value > 3:
                    return False
            elif abs(value - word1Dic[key]) > 3:
                return False

        return True