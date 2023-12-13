class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        visited = set()
        def dfs(x,y):
            
            rot = [(0,1), (1,0), (0,-1), (-1,0)]
            visited.add((x,y))
            ans = True
            for i, j in rot:
                if 0<=x+i<len(grid2) and 0<=y+j<len(grid2[0]):
                    if grid2[x+i][y+j] == 1 and grid1[x+i][y+j]==0:
                        ans = False
                    elif grid1[x+i][y+j] == grid2[x+i][y+j] == 1 and (x+i,y+j) not in visited:
                        if not dfs(x+i,y+j):
                            ans = False
            return ans
        count = 0
        for i in range(len(grid1)):
            for j in range(len(grid1[i])):
                if (i,j) not in visited and grid1[i][j] == grid2[i][j] == 1:
                    if dfs(i,j):
                        print(i,j)
                        count+=1
        return count