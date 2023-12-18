class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")]*(n+1)
        dp[0] = 0
        for i in range(n+1):
            x=1
            while x*x<=i:
                dp[i] = min(dp[i], 1+dp[i - x*x])
                x+=1
        return dp[-1]