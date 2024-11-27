# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        res = 0
    
        def dfs(root):
            if not root:
                return (True, 0, float("inf"), float("-inf"))
            
            leftSubtree = dfs(root.left)
            rightSubtree = dfs(root.right)
            
            if leftSubtree[0] and rightSubtree[0] and root.val > leftSubtree[3] and root.val < rightSubtree[2]:
                nonlocal res
                subtreeSum = leftSubtree[1] + root.val + rightSubtree[1]
                res = max(res, subtreeSum)

                # Update the minimum and maximum values of the current subtree
                return (True, subtreeSum, min(root.val, leftSubtree[2]), max(root.val, rightSubtree[3]))
            else:
                # Return invalid BST ranges for non-BST subtrees
                return (False, 0, float("-inf"), float("inf"))
        
        dfs(root)
        return res