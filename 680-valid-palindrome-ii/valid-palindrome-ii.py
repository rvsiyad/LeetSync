class Solution:
    def validPalindrome(self, s: str) -> bool:
        # What makes something a palindrome? Same backwards and forwards
        # Now how can we check if something is a palindrome if we are allowed to remove one character?
        # Check if characters are equal, if not, compare if equal if we remove the left or right character

        L = 0
        R = len(s) - 1

        while L < R:
            if s[L] != s[R]:
                removeL, removeR = s[L + 1: R + 1], s[L: R]
                return (removeL == removeL[::-1] or removeR == removeR[::-1])

            L += 1
            R -= 1
        
        return True