class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        tot = 0
        def recurse(i,j):
            nonlocal tot
            visited.add((i,j))
            rot = [(0,1), (1,0), (0,-1), (-1,0)]

            for x, y in rot:
                if i+x >= len(grid) or i+x < 0 or j+y >= len(grid[0]) or j+y < 0:
                    tot+=1
                elif grid[i+x][j+y] == 0:
                    tot+=1
                elif (i+x, y+j) not in visited:
                    recurse(i+x, y+j)
        
        found = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    recurse(i,j)
                    found = True
                    break
            if found:
                break
        
        return tot

        