# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True

        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            absoluteDiff = abs(left - right)

            nonlocal balanced

            if absoluteDiff > 1:
                balanced = False
            
            return 1 + max(right, left)
        
        dfs(root)
        return balanced