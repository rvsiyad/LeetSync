class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # We are given stones array of ints, correlat to the weught of that stone
        # We can chose any two stone from the array
        # If stones are the same weight, both stones are destroyed.
        # If one bigger than the other, the remainder is the same.

        # Not intuative at all, but the best way is to find two groups and split them into two groups
        # With the minimum difference between each other

        g1Sum = sum(stones)

        def memoization(i, g1Sum, g2Sum, cache):
            if i >= len(stones):
                return abs(g1Sum - g2Sum)
            
            if (i, g1Sum, g2Sum) in cache:
                return cache[(i, g1Sum, g2Sum)]
            
            skip = memoization(i + 1, g1Sum, g2Sum, cache)

            take = memoization(i + 1, g1Sum - stones[i], g2Sum + stones[i], cache)

            cache[(i, g1Sum, g2Sum)] = min(skip, take)

            return cache[(i, g1Sum, g2Sum)]
        
        return memoization(0, g1Sum, 0, {})