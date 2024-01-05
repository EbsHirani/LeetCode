class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = [[] for i in range(len(s))]
        wordDict = set(wordDict)
        def recurse(n):
            if n<0:
                return [[]]
            ans = []
            if dp[n]:
                return dp[n]
            for i in range(n+1):
                tempWord = s[i:n+1]
                if tempWord in wordDict:
                    # print(tempWord)
                    tempLi = recurse(i-1)
                    if tempLi:
                        for i in tempLi:
                            ans.append(i+[tempWord])
            dp[n]= ans
            return ans
        
        ans = recurse(len(s)-1)
        # print(ans)
        ans = [" ".join(i) for i in ans]
        return ans