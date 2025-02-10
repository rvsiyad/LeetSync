"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        # A doubly linked list
        # Use left as prev & right as next
        # To get sorted order in a bst, we can use inorder traversal
        # We can keep track of the first and last elements.
        # We call recurivse on left subtree
        # We need to check if we are at the first node, we can do this by checking if last element has been set
        # Now we point the current node at the first element and the first eleemtn to this node
        # Now we do the same to the right subtree
        # Call this helper function
        # Now set the first and last nodes to point at each other
        # We can return the first node?
        self.firstNode = None
        self.lastNode = None

        self.convert_to_doubly_linked_list(root)

        self.firstNode.left = self.lastNode
        self.lastNode.right = self.firstNode

        return self.firstNode
    
    def convert_to_doubly_linked_list(self, node):
        if not node:
            return None
            
        self.convert_to_doubly_linked_list(node.left)

        if not self.lastNode:
            self.firstNode = node
        else:
            node.left = self.lastNode
            self.lastNode.right = node
        
        self.lastNode = node

        self.convert_to_doubly_linked_list(node.right)