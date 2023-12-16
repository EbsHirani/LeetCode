class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        visited = [[0]*len(matrix[0]) for _ in range(len(matrix))]
        dp = [[-1]*len(matrix[0]) for _ in range(len(matrix))]
        def solve(i,j):
            if dp[i][j]!=-1:
                return dp[i][j]
            maxi = 1
            val = matrix[i][j]
            visited[i][j] = 1
            if i-1>=0 and matrix[i-1][j]>val and visited[i-1][j]==0:
                maxi = max(maxi, 1+solve(i-1, j))
                
            if i+1<len(matrix) and matrix[i+1][j]>val and visited[i+1][j]==0:
                maxi = max(maxi, 1+solve(i+1, j))
            
            if j+1<len(matrix[0]) and matrix[i][j+1]>val and visited[i][j+1]==0:
                maxi = max(maxi, 1+solve(i, j+1))
                            
            if j-1>=0 and matrix[i][j-1]>val and visited[i][j-1]==0:
                maxi = max(maxi, 1+solve(i, j-1))
            dp[i][j] = maxi
            visited[i][j]=0
            return maxi
        
        ans = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans = max(ans, solve(i,j))
        
        return ans
                
            
        