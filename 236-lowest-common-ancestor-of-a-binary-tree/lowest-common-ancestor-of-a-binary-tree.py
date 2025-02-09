# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(root):
            if not root:
                return None
            
            if p == root or q == root:
                return root
            
            left = helper(root.left)
            right = helper(root.right)

            if left and right:
                return root
            
            return left or right
        
        return helper(root)