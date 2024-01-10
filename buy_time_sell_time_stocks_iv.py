class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = {}
        def recurse(k, i, haveStock):
            if k == 0 or i>=len(prices):
                return 0
            if (k,i,haveStock) in dp:
                return dp[(k,i,haveStock)]
            if haveStock:
                ans = max(
                    recurse(k-1, i+1, False) + prices[i],
                    recurse(k,i+1,True)
                )
            else:
                ans = max(
                    recurse(k,i+1, True) - prices[i],
                    recurse(k,i+1, False)
                )
            dp[(k,i,haveStock)] = ans
            return ans
        return recurse(k,0,False)