class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        islandNum = 0
        whichIsland = [[-1]*len(grid[0]) for _ in range(len(grid))]
        queue = deque()
        visited = set()
        rot = [(0,1), (1,0), (0,-1), (-1,0)]
        def dfs(i,j):
            visited.add((i,j))
            whichIsland[i][j] = islandNum
            if islandNum == 0:
                queue.append(((i,j), 0))
            
            for x, y in rot:
                if 0<=x+i<len(grid) and 0<=y+j<len(grid[0]) and grid[x+i][y+j] ==1 and (x+i, y+j) not in visited:
                    dfs(x+i,y+j)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    if (i,j) not in visited and grid[i][j]==1:
                        dfs(i,j)
                        islandNum +=1
        
        while queue:
            (x,y), steps = queue.popleft()
            for i,j in rot:
                if 0<=x+i<len(grid) and 0<=y+j<len(grid[0]):
                    if whichIsland[x+i][y+j] == 1:
                        return steps
                    elif (x+i,y+j) not in visited:
                        queue.append(((x+i,y+j), steps+1))
                        visited.add((x+i,y+j))

        return 0