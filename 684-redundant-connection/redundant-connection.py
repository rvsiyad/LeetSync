class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # We can first create the adjList
        # Once we have the adjList
        # We go over each edge input in reverse order, see if removing that will result
        # In there not being a cycle in the adjList, return that edge.
        adjList = {i : set() for i in range(1, len(edges) + 1)}

        for n1, n2 in edges:
            adjList[n1].add(n2)
            adjList[n2].add(n1)
        
        def dfs(node, parent):            
            visited.add(node)

            for nei in adjList[node]:
                if nei == parent:
                    continue
                if nei in visited or not dfs(nei, node):
                    return False
            
            return True

        # How can we ignore the edges without having to remove them?
        for n1, n2 in reversed(edges):
            visited = set()

            # Remove them
            adjList[n1].remove(n2)
            adjList[n2].remove(n1)
            # Call dfs
            if dfs(1, -1) and len(visited) == len(edges):
                return [n1, n2]
            
            # Add them back
            adjList[n1].add(n2)
            adjList[n2].add(n1)