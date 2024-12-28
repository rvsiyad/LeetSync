class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # If we encounter a obstacle, we return 0, so another case is added to the out of bounds case
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        cache = {}

        def memoization(r, c, ROWS, COLS, cache):
            if r >= ROWS or c >= COLS or obstacleGrid[r][c] == 1:
                return 0
            
            if r == ROWS - 1 and c == COLS - 1:
                return 1
            
            if (r,c) in cache:
                return cache[(r, c)]
            
            cache[(r,c)] = (memoization(r + 1, c, ROWS, COLS, cache) + memoization(r, c + 1, ROWS, COLS, cache))

            return cache[(r,c)]
        
        return memoization(0,0, ROWS, COLS, cache)