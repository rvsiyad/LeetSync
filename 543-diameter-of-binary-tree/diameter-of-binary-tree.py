# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.maxDiameter = 0

        self.getMaxDiameter(root)

        return self.maxDiameter
    
    def getMaxDiameter(self, root):
        if not root:
            return 0
        
        left = self.getMaxDiameter(root.left)
        right = self.getMaxDiameter(root.right)

        curDiameter = left + right
        self.maxDiameter = max(curDiameter, self.maxDiameter)

        return 1 + max(right, left)