"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        pCopy, qCopy = p, q

        while pCopy != qCopy:
            pCopy = pCopy.parent if pCopy else q
            qCopy = qCopy.parent if qCopy else p
        
        return pCopy