class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 1
        for i in range(3, n+1):
            for j in range(1, i):
                print(i,j)
                dp[i] = max(dp[i], j*dp[i-j], j*(i-j))
        # print(dp)
        return dp[-1]