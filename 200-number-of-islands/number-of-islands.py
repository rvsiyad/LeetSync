class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, columns):
            ROWS, COLUMNS = len(grid) - 1, len(grid[0]) - 1

            if row < 0 or row > ROWS or columns < 0 or columns > COLUMNS or grid[row][columns] != '1':
                return
            else:
                grid[row][columns] = '0'
                dfs(row + 1, columns)
                dfs(row - 1, columns)
                dfs(row, columns + 1)
                dfs(row, columns - 1)
        
        
        numberOfIslands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    numberOfIslands += 1
                    dfs(i, j)
        
        return numberOfIslands