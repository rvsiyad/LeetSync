class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        def remove_island(row, col):
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col] == "0":
                return
            
            if grid[row][col] == "1":
                grid[row][col] = "0"
            
            remove_island(row + 1, col)
            remove_island(row - 1, col)
            remove_island(row, col + 1)
            remove_island(row, col - 1)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    num_islands += 1
                    remove_island(row, col)
        
        return num_islands