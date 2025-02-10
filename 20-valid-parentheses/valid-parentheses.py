class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openBrackets = set(['{', '(', '['])

        for string in s:
            if string in openBrackets:
                stack.append(string)
            else:
                if not stack:
                    return False
                else:
                    if string == ')' and stack[-1] == '(':
                        stack.pop()
                    elif string == ']' and stack[-1] == '[':
                        stack.pop()
                    elif string == '}' and stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
        
        return False if stack else True