class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0

        def dfs(r, c):
            ROWS, COLUMNS = len(grid) - 1, len(grid[0]) - 1

            if r < 0 or c < 0 or r > ROWS or c > COLUMNS or grid[r][c] == 0:
                return 0
            else:
                grid[r][c] = 0

                area = 1
                area += dfs(r + 1, c)
                area += dfs(r - 1, c)
                area += dfs(r, c + 1)
                area += dfs(r, c - 1)
            
            return area

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    currMax = dfs(i, j)
                    maxArea = max(maxArea, currMax)
        
        return maxArea