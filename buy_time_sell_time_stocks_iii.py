

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = [0]*len(prices)
        right = [0]*len(prices)
        leftMin = prices[0]
        rightMax = prices[-1]

        for i in range(1, len(prices)):
            leftId = i
            rightId = len(prices)-i-1
            left[leftId] = max(left[leftId-1], prices[leftId]-leftMin)
            right[rightId] = max(right[rightId+1], rightMax - prices[rightId])
            leftMin = min(leftMin, prices[leftId])
            rightMax = max(rightMax, prices[rightId])
        ans = 0
        for i in range(len(prices)):
            ans = max(ans, left[i]+right[i])
        return ans