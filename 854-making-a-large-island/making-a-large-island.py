class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        """
        - Go through islands, find the islands that are connected and change the ids to a matching id for that island.
        - We should also calculate the area for that island by counting the number of 1s using DFS
        - Save to a hashmap where the key is the island id we changed them to and the area that island takes up
        - Next we go through the matrix again, creating a visited set, the area is gonna be the 1 + the islands seen areas.
        - We need to check if area is greater than 1 or else we have a matrix of just 1s, return row * columns
        """
        ROWS, COLS = len(grid), len(grid[0])

        islandAreas = {}
        self.islandId = -1
        self.islandArea = 0
        self.directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    self.changeOnesToIslandId(grid, row, col)

                    islandAreas[self.islandId] = self.islandArea

                    self.islandId -= 1
                    self.islandArea = 0
        
        maxArea = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    area = 1
                    visited = set()

                    for dr, dc in self.directions:
                        newRow = row + dr
                        newCol = col + dc

                        if newRow < 0 or newRow >= ROWS or newCol < 0 or newCol >= COLS or grid[newRow][newCol] == 0 or grid[newRow][newCol] in visited:
                            continue

                        # if (
                        #     newRow >= 0 and newRow < ROWS and
                        #     newCol >= 0 and newCol < COLS and
                        #     grid[newRow][newCol] != 0 and grid[newRow][newCol] not in visited
                        #     ):
                        
                        area += islandAreas[grid[newRow][newCol]]
                        
                        visited.add(grid[newRow][newCol])
                    
                    maxArea = max(maxArea, area)
        
        return maxArea if maxArea > 0 else ROWS * COLS



    
    def changeOnesToIslandId(self, grid, row, col):
        ROWS, COLS = len(grid), len(grid[0])

        if row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col] != 1:
            return
        
        grid[row][col] = self.islandId
        self.islandArea += 1

        for dr, dc in self.directions:
            newRow = row + dr
            newCol = col + dc

            self.changeOnesToIslandId(grid, newRow, newCol)