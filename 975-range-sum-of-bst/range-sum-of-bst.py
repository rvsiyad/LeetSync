# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        queue = deque()
        total = 0

        queue.append(root)

        while queue:
            node = queue.popleft()

            if node.val >= low and node.val <= high:
                total += node.val
            
            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
        
        return total
        