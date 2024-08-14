# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        def backtrack(root, curr):
            if not root:
                return

            curr.append(root.val)

            if not root.left and not root.right:
                result = "->".join(map(str, curr))
                res.append(result)
            else:
                backtrack(root.left, curr)
                backtrack(root.right, curr)
            
            curr.pop()
            
        
        backtrack(root, [])
        return res
            


            

