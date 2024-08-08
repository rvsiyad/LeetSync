# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(root, targetSum, curTotal):
            if not root:
                return False
            
            curTotal += root.val
            if not root.left and not root.right and targetSum == curTotal:
                return True
            
            if helper(root.left, targetSum, curTotal):
                return True
            if helper(root.right, targetSum, curTotal):
                return True
            
            return False
        
        return helper(root, targetSum , 0)