class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = {(a, b) for a, b in connections}
        adjList = {city: [] for city in range(n)}

        visited = set()
        changes = 0

        for a, b in connections:
            adjList[a].append(b)
            adjList[b].append(a)
        
        def dfs(city):
            nonlocal changes,visited, edges, adjList

            for nei in adjList[city]:
                if nei in visited:
                    continue
                
                if (nei, city) not in edges:
                    changes += 1
                
                visited.add(nei)
                dfs(nei)
        
        visited.add(0)
        dfs(0)

        return changes