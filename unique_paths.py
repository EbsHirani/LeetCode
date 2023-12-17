class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        for i in range(n):
            dp[-1][i] = 1
        for i in range(m):
            dp[i][-1] = 1
        
        for i in reversed(range(m-1)):
            for j in reversed(range(n-1)):
                dp[i][j] = dp[i][j+1] + dp[i+1][j]
        
        return dp[0][0]