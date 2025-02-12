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
        if not node:
            return None

        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            newNode = Node(node.val)
            oldToNew[node] = newNode

            for nei in node.neighbors:
                newNode.neighbors.append(dfs(nei))
            
            return newNode
        
        dfs(node)
    
        return oldToNew[node]

