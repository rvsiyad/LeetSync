class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # If it is impossible to make the trip with the current values, we can return float("inf")
        # If we buy 7 days, we incur the cost of that day
        # Base cases -> (if in cache, return cached), (if out of bounds)

        # We need to know if ticket we buy will cover the days we are travelling. Can do this by
        # creating a day can travel variable, reduces by the differnce between days. Minus the previous value if i > 0, if this
        # path does not leave positive days remaining, return float("inf")

        def memoization(i, cache):
            if i in cache:
                return cache[i]
            
            if i >= len(days):
                return 0
            
            cache[i] = float("inf")

            for day, cost in zip([1,7,30], costs):
                j = i

                while j < len(days) and days[j] < days[i] + day:
                    j += 1
                
                cache[i] = min(cache[i], cost + memoization(j, cache))
            
            return cache[i]
        
        return memoization(0, {})

