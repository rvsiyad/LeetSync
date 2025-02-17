class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split(" ")

        validWords = [word for word in words if word]

        return len(validWords[-1])