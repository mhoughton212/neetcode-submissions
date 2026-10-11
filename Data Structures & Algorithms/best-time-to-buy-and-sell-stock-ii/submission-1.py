class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        res = 0
        profit = 0
        for r in range(len(prices) - 1):
            if prices[r] > prices[r + 1]:
                res += prices[r] - prices[l]
                l = r + 1
            
        return res + prices[len(prices) - 1] - prices[l]