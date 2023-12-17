class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False]*len(s) for _ in range(len(s))]
        maxi=1
        ans = s[0]
        for i in range(len(s)):
            dp[i][i] = True
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                maxi= 2
                ans = s[i:i+2]
        for i in range(2, len(s)):
            for j in range(len(s)-i):
                # print(j,j+i, len(s))
                if s[j] == s[j+i] and dp[j+1][j+i-1]:
                    dp[j][j+i] = True
                    maxi = i+1
                    ans = s[j:j+i+1]
        return ans