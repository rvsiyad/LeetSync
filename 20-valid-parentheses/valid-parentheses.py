class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i in '([{':
                stack.append(i)
            else:
                if not stack:
                    return False
                
                poppedVal = stack.pop()

                if i == ')' and poppedVal != '(':
                    return False
                elif i == '}' and poppedVal != '{':
                    return False
                elif i == ']' and poppedVal != '[':
                    return False
        
        if stack:
            return False
        else:
            return True