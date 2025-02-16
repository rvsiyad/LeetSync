"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
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
        

        