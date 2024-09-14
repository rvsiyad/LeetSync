class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def dfs(r, c, visited):
            ROWS, COLUMNS = len(grid), len(grid[0])

            if r < 0 or c < 0 or r == ROWS or c == COLUMNS or grid[r][c] == 0:
                return 1
            
            if (r,c) in visited:
                return 0
            
            visited.add((r,c))

            perimeter = 0

            perimeter += dfs(r + 1, c , visited)
            perimeter += dfs(r - 1, c , visited)
            perimeter += dfs(r, c -1 , visited)
            perimeter += dfs(r, c + 1 , visited)

            return perimeter

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return dfs(r, c, set())
        
        return 0