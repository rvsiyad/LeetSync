"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution(object):
    def lowestCommonAncestor(self, p, q):
        """
        :type node: Node
        :rtype: Node
        """
        pPointer, qPointer = p, q
        while pPointer != qPointer:
            pPointer = pPointer.parent if pPointer else q
            qPointer = qPointer.parent if qPointer else p

        return pPointer
