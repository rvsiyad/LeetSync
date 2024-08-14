# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = []

        def dfs(root, curDepth):
            if not root:
                res.append(curDepth)
                return None
            
            curDepth += 1

            dfs(root.left, curDepth)
            dfs(root.right, curDepth)

        dfs(root, 0)
        return max(res)
