"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        
        self.firstNode = None
        self.lastNode = None

        self.convertBinarySearchTreeToLL(root)

        self.firstNode.left = self.lastNode
        self.lastNode.right = self.firstNode

        return self.firstNode
    
    def convertBinarySearchTreeToLL(self, node):
        if not node:
            return
        
        self.convertBinarySearchTreeToLL(node.left)

        if not self.lastNode:
            self.firstNode = node
        else:
            node.left = self.lastNode
            self.lastNode.right = node
        
        self.lastNode = node

        self.convertBinarySearchTreeToLL(node.right)

