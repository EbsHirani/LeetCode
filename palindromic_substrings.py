class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False]*(len(s)) for _ in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = True
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
        
        for diff in range(2, len(s)):
            for i in range(len(s)-diff):
                start = i
                end = i+diff
                if s[start] == s[end] and dp[start+1][end-1]:
                    dp[start][end] = True
        count = 0
        for i in dp:
            for j in i:
                if j:
                    count+=1
        return count