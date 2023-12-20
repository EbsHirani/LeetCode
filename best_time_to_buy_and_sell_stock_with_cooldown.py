class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<=1:
            return 0
        have_stock = [0]*len(prices)
        no_stock = [0]*len(prices)

        have_stock[0] = -prices[0]
        no_stock[0] = 0

        have_stock[1] = -min(prices[0], prices[1])
        no_stock[1] = max(0,prices[1]-prices[0])

        for i in range(2,len(prices)):
            have_stock[i] = max(have_stock[i-1], no_stock[i-2] - prices[i])
            no_stock[i] = max(no_stock[i-1], have_stock[i-1] + prices[i])
        return no_stock[-1]