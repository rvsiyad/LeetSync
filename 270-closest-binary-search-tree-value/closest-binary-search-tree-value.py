# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        # Traverse the tree, if not root return
        # Create a gloabl varaibles to compare

        # How to keep track of closest to target, find the min absolute difference between them
        # Create a minDiff variable, closestNum variable
        # Keep updating the minDiff, if minDiff is the same, update closest with the smaller between the closest num and current
        self.minDiff = float("inf")
        self.closestNum = float("inf")

        def dfs(node, target):
            if not node:
                return
            
            diff = abs(target - node.val)

            if diff < self.minDiff:
                self.minDiff = diff
                self.closestNum = node.val
            elif diff == self.minDiff and node.val < self.closestNum:
                self.closestNum = node.val
            
            dfs(node.left, target)
            dfs(node.right, target)
        
        dfs(root, target)

        return self.closestNum

            


