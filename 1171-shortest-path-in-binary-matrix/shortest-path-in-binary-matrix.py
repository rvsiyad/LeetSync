from collections import deque

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        ROWS, COLS = len(grid), len(grid[0])

        if grid[0][0] == 1 or grid[ROWS -1][COLS -1] == 1:
            return -1

        queue = deque()
        length = 1
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]

        queue.append([0, 0])
        visited = set()

        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                if row == ROWS -1 and col == COLS -1:
                    return length

                for dr, dc in directions:
                    newRow, newCol = row + dr, col + dc

                    if newRow < 0 or newRow >= ROWS or newCol < 0 or newCol >= COLS or (newRow, newCol) in visited or grid[newRow][newCol] == 1:
                        continue
                    
                    queue.append((newRow, newCol))
                    visited.add((newRow, newCol))
            
            length += 1
        
        
        return -1