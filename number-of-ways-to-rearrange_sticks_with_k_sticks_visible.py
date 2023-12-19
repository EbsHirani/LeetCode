class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        MOD = 1000000007
        dp = [[-1]*(k+1) for _ in range(n+1)]
        def recurse(candles, visible):
            if candles==visible:
                return 1
            if candles<visible or visible==0:
                return 0
            if dp[candles][visible] !=-1:
                return dp[candles][visible]
            ans= recurse(candles-1,visible-1)%MOD + (candles-1)*recurse(candles-1, visible)%MOD
            dp[candles][visible] = ans%MOD

            return dp[candles][visible]
        return recurse(n,k) 
        