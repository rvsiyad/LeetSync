# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: Optional[TreeNode]
        :type target: float
        :rtype: int
        """
        self.minDiff = float("inf")
        self.closestNum = float("inf")

        def dfs(node):
            if not node:
                return
            
            diff = abs(target - node.val)

            if diff < self.minDiff:
                self.minDiff = diff
                self.closestNum = node.val
            elif diff == self.minDiff:
                self.closestNum = node.val if node.val < self.closestNum else self.closestNum
            
            if node.val < target:
                dfs(node.right)
            else:
                dfs(node.left)
        
        dfs(root)
        return self.closestNum