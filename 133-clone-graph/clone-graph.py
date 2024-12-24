"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:return None
        
        oldToNew = {}

        def dfs(oldNode):
            if oldNode in oldToNew:
                return oldToNew[oldNode]
            
            newNode = Node(oldNode.val)
            oldToNew[oldNode] = newNode

            for neigh in oldNode.neighbors:
                newNode.neighbors.append(dfs(neigh))
            
            return newNode
        
        return dfs(node)
            

