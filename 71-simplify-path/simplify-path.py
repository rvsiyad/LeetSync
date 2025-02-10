class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        pathItems = path.split("/")

        for item in pathItems:
            if item in ['.','']:
                continue
            
            elif item == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(item)

        return "/" + "/".join(stack)
