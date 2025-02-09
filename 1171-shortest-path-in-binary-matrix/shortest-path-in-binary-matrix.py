from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        if grid[0][0] == 1 or grid[ROWS - 1][COLS-1] == 1:
            return -1

        queue = deque()

        queue.append((0, 0))
        grid[0][0] = 1

        length = 1

        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                if row == ROWS - 1 and col == COLS - 1:
                    return length
                
                directions = [[0, 1], [1, 0], [-1, 0], [0, -1], [-1, 1], [1, -1], [-1, -1], [1, 1]]

                for dr, dc in directions:
                    newRow, newCol = row + dr, col + dc

                    if newRow < 0 or newRow >= ROWS or newCol < 0 or newCol >= COLS or grid[newRow][newCol] == 1:
                        continue
                    
                    grid[newRow][newCol] = 1
                    queue.append((newRow, newCol))
            
            length += 1
        
        return -1