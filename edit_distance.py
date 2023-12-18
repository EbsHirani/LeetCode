class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[-1]*len(word2) for _ in range(len(word1))]
        def recurse(i,j):
            if i>=len(word1):
                return len(word2)-j
            if j>=len(word2):
                return len(word1)-i
            if dp[i][j]!=-1:
                return dp[i][j]
            if word1[i] == word2[j]:
                ans = recurse(i+1,j+1)
            else:
                ans =1+ min(recurse(i,j+1), recurse(i+1,j), recurse(i+1,j+1))
            dp[i][j] = ans
            return ans
        return recurse(0,0)