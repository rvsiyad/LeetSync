# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDepth = 0

        def dfs(root):
            if not root:
                return 0
            
            nonlocal maxDepth
            
            left = dfs(root.left)
            right = dfs(root.right)

            maxDepth = max(maxDepth, right + left)

            return 1 + max(right, left)

        dfs(root)
        return maxDepth