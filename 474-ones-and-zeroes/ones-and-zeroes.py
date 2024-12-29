class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # Create a count of the number of 1s and 0 for values at i in strs
        counter = {}
        cache = {}

        for i in range(len(strs)):
            zeroAndOnes = Counter(strs[i])
            counter[i] = [zeroAndOnes["0"], zeroAndOnes["1"]]
        
        def memoization(i, m, n, zeroCount, oneCount, counter, cache):
            if i >= len(strs):
                return 0
            
            if (i, zeroCount, oneCount) in cache:
                return cache[(i, zeroCount, oneCount)]
            
            skip = memoization(i + 1, m, n, zeroCount, oneCount, counter, cache)

            zeros, ones = counter[i]

            maxValue = skip

            if (zeroCount + zeros) <= m and (oneCount + ones) <= n:
                take = 1 + memoization(i + 1, m, n, zeroCount + zeros, oneCount + ones, counter, cache)

                maxValue = max(maxValue, take)
            
            cache[(i, zeroCount, oneCount)] = maxValue

            return cache[(i, zeroCount, oneCount)]
        
        return memoization(0, m, n, 0, 0, counter, cache)



        # We can use dynamic programming to see if we should take or skip this value
        # If counts of 0 and 1 are under m and n, we can return 1 and the cached previous values.
        
        # We only want to include this value if the adding of it will not exceeed the m and n amounts!!!