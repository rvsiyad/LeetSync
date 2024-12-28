class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # This can be down using dynamic programming, we can use the base cases and return all possible unique paths
        # from the top left all the way to the bottom right. All squares have a number of unique paths from itself to
        # The bottom right, it is the addition of all right paths plus all bottom paths. This is what we will cache.

        # Although we are given a matrix, we dont necessarily have to even create matrix, can just reference it.
        ROWS = m
        COLS = n
        cache = {}

        def memoization(r, c, ROWS, COLS, cache):
            if r >= ROWS or c >= COLS:
                return 0
            
            if r == ROWS - 1 and c == COLS - 1:
                return 1
            
            if (r, c) in cache:
                return cache[(r, c)]
            
            cache[(r, c)] = (memoization(r + 1, c, ROWS, COLS, cache) + memoization(r, c + 1, ROWS, COLS, cache))

            return cache[(r, c)]
        
        return memoization(0, 0, ROWS, COLS, cache)