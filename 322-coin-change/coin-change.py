class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # We are tasked with creating the amount 11, from the fewest coins used.
        # If we exceed the len of coins or we currently have more than amount (assuming we can't have negatives), return 0
        # We create a coins count, keep track of number of coins used.
        # How do we account for if we cannot make the desired amount? Since we want to return the minimum, if we return -1
        # We can check if any of the paths return -1, if both are -1, return -1, return the one that isnt -1
        def momoization(i, amount, cache):
            if (i, amount) in cache:
                return cache[(i, amount)]
            
            if amount == 0:
                return 0
            
            if i >= len(coins) or amount < 0:
                return float("inf")
            
            skip = momoization(i + 1, amount, cache)

            take = 1 + momoization(i, amount - coins[i], cache)
            
            cache[(i, amount)] = min(skip, take)
            
            return cache[(i, amount)]
        
        result = momoization(0, amount, {})

        return result if result != float("inf") else -1