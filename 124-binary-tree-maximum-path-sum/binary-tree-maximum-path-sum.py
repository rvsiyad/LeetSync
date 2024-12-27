# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # We need to dfs and find the max sum, we can either include the sum or not include it
        # Create a global max sum variable which we can update to keep track
        # We will not include a path if it is not atleast zero.
        # We will return the max between either the left or right subtrees of the binary tree.
        maxSum = float("-inf")

        def dfs(root):
            if not root:
                return 0
            
            left = max(0, dfs(root.left))
            right = max(0, dfs(root.right))

            nonlocal maxSum
            maxSum = max(maxSum, root.val + left + right)

            return root.val + max(left, right)
        
        dfs(root)
        return maxSum