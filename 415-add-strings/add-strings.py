class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i = len(num1) - 1
        j = len(num2) - 1

        carry = 0
        res = []

        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0

            curSum = n1 + n2 + carry

            res.append(str(curSum % 10))
            carry = curSum // 10

            i -= 1
            j -= 1
        
        if carry:
            res.append(str(carry))

        return "".join(reversed(res))