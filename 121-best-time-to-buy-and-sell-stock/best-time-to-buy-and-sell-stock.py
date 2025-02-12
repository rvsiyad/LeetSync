class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        greatestProfit = 0
        L = 0

        for R in range(1, len(prices)):
            if prices[L] > prices[R]:
                L = R
            else:
                greatestProfit = max(greatestProfit, prices[R] - prices[L])

        return greatestProfit