# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k == 0:
            return [target.val]

        # We need to find all nodes connected to the current node.
        # We can do this by creating an adjList of the currentNode and its connections
        connectedNodes = collections.defaultdict(list)

        # DFS to create the adjList and then BFS to keep to distance of k?
        def dfs(node):
            if not node:
                return 
            
            if node.left:
                connectedNodes[node].append(node.left)
                connectedNodes[node.left].append(node)
                dfs(node.left)
            
            if node.right:
                connectedNodes[node].append(node.right)
                connectedNodes[node.right].append(node)
                dfs(node.right)
        
        dfs(root)
        # Now we have all the nodes, we need to DFS to k distance, add those nodes to result, we also do not want to revist nodes

        visited = set()
        visited.add(target)
    
        res = []

        def findKDistanceNodes(node, distance):    
            if distance == k:
                res.append(node.val)
                return
            
            for nei in connectedNodes[node]:
                if nei not in visited:
                    visited.add(nei)
                    findKDistanceNodes(nei, distance + 1)

        findKDistanceNodes(target, 0)
        return res


            
            