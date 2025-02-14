class Solution(object):
    def getFood(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        queue = collections.deque()
        visited = set()
        shortestPath = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        ROWS, COLS = len(grid), len(grid[0])

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "*":
                    queue.append((row, col))

        while queue:
            for i in range(len(queue)):
                row, col = queue.popleft()

                if row < 0 or row == ROWS or col < 0 or col == COLS or (row, col) in visited or grid[row][col] == 'X':
                    continue

                visited.add((row, col))

                if grid[row][col] == '#':
                    return shortestPath
                
                for dr, dc in directions:
                    newRow, newCol = row + dr, col + dc
                    queue.append((newRow, newCol))
            
            shortestPath += 1
        
        return -1

"""
[["X","X","X","X","X"],
["X","*","X","O","X"],
["X","O","X","#","X"],
["X","X","X","X","X"]]
"""