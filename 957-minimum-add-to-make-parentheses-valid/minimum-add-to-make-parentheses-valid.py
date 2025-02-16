class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0

        stack = []

        for bracket in s:
            if bracket == "(":
                stack.append(bracket)
                count += 1
            else:
                if stack:
                    stack.pop()
                    count -= 1
                else:
                    count += 1
        
        return count