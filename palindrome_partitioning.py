class Solution:
    def minCut(self, s: str) -> int:
        dp = [float("inf")]*len(s)

        for i in reversed(range(len(s))):
            sub = s[i:]
            if sub == sub[::-1]:
                dp[i] = 0
                continue
            
            for j in range(i+1, len(s)):
                sub = s[i:j]
                if sub == sub[::-1]:
                    dp[i] = min(1+dp[j], dp[i])
        return dp[0]