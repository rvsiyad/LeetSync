class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        """
        Use a monotonic decreasing stack, we keep popping from the stack if the new value we want to add is greater
        than the previously added height. We add the indexes to the stack

        Example:
        heights = [4,2,3,1]
        indexes = [0,1,2,3]

        stack = [0,2,]
        """
        stack = []

        for i in range(len(heights)):
            if stack:
                while stack and heights[i] >= heights[stack[-1]]:
                    stack.pop()

            stack.append(i)
        
        return stack