class Solution:
    def numTrees(self, n: int) -> int:
        dp = [[0]*n for _ in range(n)]
        def recurse(start,end):
            if end<=start:
                return 1
            if end-start == 1:
                return 2
            if dp[start-1][end-1] != 0:
                return dp[start-1][end-1]
            ans = 0
            for i in range(start,end+1):
                ans += recurse(start, i-1)*recurse(i+1,end)
            dp[start-1][end-1] = ans
            return ans
            
        return recurse(1,n)