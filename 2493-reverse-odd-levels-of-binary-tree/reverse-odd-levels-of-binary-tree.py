# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Take a BFS approach, count the level we are at, if level is odd, we swap children
        queue = deque()
        queue.append(root)

        level = 0

        while queue:
            if level % 2 != 0:
                L = 0
                R = len(queue) - 1
                while L < R:
                    queue[L].val, queue[R].val = queue[R].val, queue[L].val
                    R -= 1
                    L += 1

            for i in range(len(queue)):
                node = queue.popleft()
                
                if node.right:
                    queue.append(node.right)
                
                if node.left:
                    queue.append(node.left)
            
            level += 1
        
        return root
