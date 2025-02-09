# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Create a map to hold values at each x axis
        # Create a queue, BFS tracking the current x axis value and the node
        # SInce we need to return the order from L to R, Keep track of min x and max x values.

        if not root:
            return []

        axisValues = collections.defaultdict(list)
        minX = float("inf")
        maxX = float("-inf")

        queue = collections.deque()
        queue.append((0, root))

        while queue:
            for i in range(len(queue)):
                xAxis, node = queue.popleft()

                axisValues[xAxis].append(node.val)

                minX = min(minX, xAxis)
                maxX = max(maxX, xAxis)

                if node.left:
                    queue.append((xAxis - 1, node.left))
                
                if node.right:
                    queue.append((xAxis + 1, node.right))
        
        print(axisValues)
        result = []
        for i in range(minX, maxX + 1):
            result.append(axisValues[i])
        
        return result