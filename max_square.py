class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[-1]*len(matrix[0]) for _ in range(len(matrix))]
        def recurse(i,j):
            # print(i,j)
            if i>=len(matrix) or j>=len(matrix[0]):
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            if matrix[i][j]=="1":
                dp[i][j] = 1 + min(recurse(i,j+1), recurse(i+1,j), recurse(i+1,j+1))
            else:
                dp[i][j] = 0
            return dp[i][j]
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                ans = max(recurse(i,j), ans)
        return ans*ans