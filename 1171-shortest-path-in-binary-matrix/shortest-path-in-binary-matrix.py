class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLUMNS = len(grid), len(grid[0])

        if grid[0][0] == 1 or grid[ROWS -1][COLUMNS -1] == 1:
            return -1

        queue = collections.deque()
        queue.append((0,0))

        grid[0][0] = 1

        length = 1

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                if r == ROWS -1 and c == COLUMNS -1:
                    return length

                directions = [[0,1],[0,-1], [1,0], [-1,0], [1,1], [1,-1], [-1, 1], [-1,-1]]

                for dr, dc in directions:
                    newRow = r + dr
                    newColumn = c + dc

                    if newRow < 0 or newColumn < 0 or newRow == ROWS or newColumn == COLUMNS or grid[newRow][newColumn] == 1:
                        continue
                    
                    grid[newRow][newColumn] = 1
                    queue.append((newRow, newColumn))

            length += 1
        return -1
