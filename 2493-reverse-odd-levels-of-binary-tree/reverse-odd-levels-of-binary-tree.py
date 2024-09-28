# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(nodeL, nodeR, level):
            if not nodeL or not nodeR:
                return None
            
            if level % 2 != 0:
                nodeL.val, nodeR.val = nodeR.val, nodeL.val
            
            dfs(nodeL.left, nodeR.right, level + 1)
            dfs(nodeL.right, nodeR.left, level + 1)

        dfs(root.left, root.right, 1)

        return root