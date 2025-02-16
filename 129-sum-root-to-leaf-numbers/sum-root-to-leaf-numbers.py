# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        self.total = 0

        def helper(node, curSum):
            if not node:
                return
            else:
                curSum = (curSum * 10) + node.val

                if not node.left and not node.right:
                    self.total += curSum
                    return

                helper(node.left, curSum)
                helper(node.right, curSum)
        
        helper(root, 0)
        return self.total

        