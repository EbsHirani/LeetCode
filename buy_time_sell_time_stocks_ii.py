class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        haveStock = -prices[0]
        dontHaveStock = 0

        for i in range(1, len(prices)):

            tempHaveStock = max(haveStock, dontHaveStock - prices[i])
            dontHaveStock = max(haveStock + prices[i], dontHaveStock)

            haveStock = tempHaveStock
        return dontHaveStock

