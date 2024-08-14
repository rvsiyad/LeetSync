# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Think about it in two ways.
        # First we portion of this problem is finding the two root nodes that match for the root and subRoot trees.
        # The next portion is to see if both trees from then on match.
        if not root and not subRoot:
            return False
        
        if not root and subRoot:
            return False
        
        if not subRoot and root:
            return True

        if root.val == subRoot.val:
            if self.isTheSameTree(root, subRoot):
                return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    #Create a helper function to see if both trees are the same.
    def isTheSameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        if root and not subRoot:
            return False
        if subRoot and not root:
            return False
        if root.val == subRoot.val and root and subRoot:
            return self.isTheSameTree(root.left, subRoot.left) and self.isTheSameTree(root.right, subRoot.right)
        return False 