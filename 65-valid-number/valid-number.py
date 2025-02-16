class Solution(object):
    def isNumber(self, s):
        deciamlSeen = False
        numberSeen = False

        i = 0

        if s[i] in ['+', '-']:
            i += 1
        
        while i < len(s):
            if s[i].isdigit():
                numberSeen = True
            elif s[i] in ['e', 'E']:
                return numberSeen and self.validExponent(s[i + 1:])
            elif s[i] == '.':
                if deciamlSeen:
                    return False
                else:
                    deciamlSeen = True
            else:
                return False
            
            i += 1
        
        return numberSeen
    
    def validExponent(self, s):
        if not s:
            return False
        
        numberSeen = False
        i = 0

        if s[i] in ['+', '-']:
            i += 1
        
        while i < len(s):
            if s[i].isdigit():
                numberSeen = True
                i += 1
            else:
                return False
        
        return numberSeen