class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        org_count = 0
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    org_count+=1
                elif grid[i][j] == 2:
                    queue.append((i,j,0))
        
        rot = [(0,1), (1,0), (-1,0), (0,-1)]
        t=0
        while queue:
            x,y,t = queue.popleft()
            for i,j in rot:
                if 0<=x+i<len(grid) and 0<=y+j<len(grid[0]) and grid[x+i][y+j] == 1:
                    grid[x+i][y+j] = 2
                    queue.append((x+i, y+j, t+1))
                    org_count-=1
                
        if org_count == 0:
            return t
        return -1