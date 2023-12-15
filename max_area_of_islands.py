class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited = [[-1]*len(grid[0]) for _ in range(len(grid))]
        def solve(i,j):
            ret = 1
            if visited[i][j]!=-1:
                return 0
            
            else:
                visited[i][j]= 1
                if i+1<len(grid) and grid[i+1][j]==1:
                    ret+=solve(i+1,j)
                if i-1>=0 and grid[i-1][j]==1:
                    ret+=solve(i-1,j)
                if j+1<len(grid[0]) and grid[i][j+1]:
                    ret+=solve(i,j+1)
                if j-1>=0 and grid[i][j-1]:
                    ret+=solve(i,j-1)
            
            # print(i,j,ret)
            return ret

        ans = 0  
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    ans = max(ans, solve(i,j))
        
        return ans
        