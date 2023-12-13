class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        queue = set()
        queue.add((0,0))
        val = [[float("inf")]*len(grid[0]) for _ in range(len(grid))]

        val[0][0] = grid[0][0]
        rot = [(0,1), (1,0), (0,-1), (-1,0)]
        while queue:
            x,y = min(queue, key = lambda x : val[x[0]][x[1]])
            queue.remove((x,y))
            if x==len(grid)-1 and y == len(grid[0])-1:
                return val[x][y]
            for i,j in rot:
                if 0<=x+i<len(grid) and 0<=y+j<len(grid[0]):
                    if val[x+i][y+j] > max(grid[x+i][y+j], val[x][y]):
                        val[x+i][y+j] = max(grid[x+i][y+j], val[x][y])
                        queue.add((x+i, y+j))
        
        return val[x][y]