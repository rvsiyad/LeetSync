class Solution(object):
    def isValid(self, s):
        stack = []

        for bracket in s:
            if bracket in ['{', '[', '(']:
                stack.append(bracket)
            else:
                if stack:
                    if bracket == '}' and stack[-1] == '{':
                        stack.pop()
                    elif bracket == ']' and stack[-1] == '[':
                        stack.pop()
                    elif bracket == ')' and stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        
        return False if stack else True
