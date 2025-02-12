class Solution:
    def isNumber(self, s: str) -> bool:
        """
        - If we encounter a letter other than "e" or "E", return False
        - If we see a '+' or '-', we cannot seen another until after an exponent(e or E)
        - If we see a deciaml, we cannot seen one again, even after e
        - We must see a number at some point
        """

        numberSeen = False
        decimalSeen = False

        i = 0

        if s[i] in ['+', '-']:
            i += 1
        
        while i < len(s):
            if s[i] in ['e', 'E']:
                return numberSeen and self.isValidPostExponent(s[i+ 1:])
            elif s[i].isdigit():
                numberSeen = True
            elif s[i] == '.':
                if decimalSeen:
                    return False
                else:
                    decimalSeen = True
            elif s[i] in ['+', '-']:
                return False
            else:
                return False
            
            i += 1
        
        return numberSeen
    

    def isValidPostExponent(self, postExponent):
        if not postExponent:
            return False
        
        numberSeen = False

        i = 0

        if postExponent[i] in ['+', '-']:
            i += 1
        
        while i < len(postExponent):
            if postExponent[i].isdigit():
                numberSeen = True
            elif not postExponent[i].isdigit():
                return False
            
            i += 1
        
        return numberSeen
                