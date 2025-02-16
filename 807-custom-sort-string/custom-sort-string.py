class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        sCount = {}

        for char in s:
            sCount[char] = 1 + sCount.get(char, 0)
        
        result = ""

        for letter in order:
            if letter in sCount:
                result += letter * sCount[letter]
                del sCount[letter]
        
        for letter, count in sCount.items():
            result += letter * count
        
        return result