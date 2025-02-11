# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # Only once we reach the root, we should add the path totals to a global variable.
        self.total = 0

        def dfs(node, currentSum):
            if not node:
                return
    
            currentSum = (currentSum * 10) + node.val

            if not node.right and not node.left:
                self.total += currentSum
                return
            
            if node.left:
                dfs(node.left, currentSum)
            
            if node.right:
                dfs(node.right, currentSum)
        
        dfs(root, 0)

        return self.total