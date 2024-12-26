class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Left pointer we move when we find a smaller starting price on the right pointer
        # Each time we encounter a value, we take the max (diff)
        L = 0
        maxProfit = float("-inf")

        for R in range(1, len(prices)):
            if prices[R] < prices[L]:
                L = R
                continue
            
            maxProfit = max(maxProfit,prices[R] - prices[L])
        
        return 0 if maxProfit == float("-inf") else maxProfit
