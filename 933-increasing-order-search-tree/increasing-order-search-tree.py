# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Get the inorder of the original tree, then we use that to create a new tree with just the right children
        inOrder = []

        def dfs(root):
            if not root:
                return
            
            nonlocal inOrder
            
            dfs(root.left)
            inOrder.append(root.val)
            dfs(root.right)
        
        dfs(root)
        
        newNode = TreeNode()
        curr = newNode

        for i in inOrder:
            nextNode = TreeNode(i)
            curr.right = nextNode
            curr = curr.right
        
        return newNode.right
