class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        """
        - Keep track of the count
        - If s[i] == '(', we add to stack, increment count by 1
        - If s[i] == ')'
            - If stack:
                - If stack[-1] == '(':
                    - Count -= 1
                    - Pop from stack
            count += 1
        
        - return count
        """
        count = 0
        stack = []

        for i in s:
            if i == '(':
                stack.append(i)
                count += 1
            else:
                if stack and stack[-1] == '(':
                        count -= 1
                        stack.pop()
                else:
                    count += 1
        
        return count

