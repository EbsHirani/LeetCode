class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(1,len(s)+1):
            for j in range(0,i):
                if dp[j] and s[j:i]in wordDict:
                    dp[i] = True
                    break
        
        return dp[-1]