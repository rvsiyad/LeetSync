class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(row, col):
            if (row, col) in visited:
                return 0
            
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col] == 0:
                return 1
            
            visited.add((row, col))

            return dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1)

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    return dfs(row, col)