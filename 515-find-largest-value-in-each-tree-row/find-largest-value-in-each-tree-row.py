# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # BFS approach, go through each layer in the tree, create a max variable for each queue iteration
        # Keep track and update maxVal, append to result array at end of each queue iteration.
        if not root:
            return []
        
        queue = deque()
        result = []

        queue.append(root)

        while queue:
            maxVal = float("-inf")

            for i in range(len(queue)):
                node = queue.popleft()

                maxVal = max(node.val, maxVal)

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            result.append(maxVal)
        
        return result