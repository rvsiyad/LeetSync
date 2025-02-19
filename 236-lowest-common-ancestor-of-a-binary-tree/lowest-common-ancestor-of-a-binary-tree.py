# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def helper(node):
            if not node:
                return None
            
            if node == p or node == q:
                return node
            
            left = helper(node.left)
            right = helper(node.right)

            if left and right:
                return node
            
            return left or right
        
        return helper(root)