class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        stack = []

        for i in words:
            stack.append(i)

            if len(stack) > 1 and sorted(stack[-1]) == sorted(stack[-2]):
                stack.pop()

        return stack
