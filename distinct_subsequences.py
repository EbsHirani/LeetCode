class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[-1]*len(t) for _ in range(len(s))]
        def recurse(i,j):
            if j == len(t):
                return 1
            if i== len(s):
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            ans = 0
            if s[i] == t[j]:
                ans+=recurse(i+1,j+1)
            ans+=recurse(i+1,j)
            dp[i][j] = ans
            return ans
        return recurse(0,0)