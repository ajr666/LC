class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0] # price[i]左边的最小值
        ans = 0
        for i in range(1, len(prices)):
            ans = max(prices[i] - minPrice, ans)
            minPrice = min(minPrice, prices[i])

        return ans
        