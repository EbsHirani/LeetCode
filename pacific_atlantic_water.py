class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacVisited = set()
        atVisited = set() 
        def recurse(r,c, visited):
            visited.add((r,c))
            
            rot = [(0,1), (1,0), (0,-1), (-1,0)]
            for i, j in rot:
                isBoundary = False
                if r+i < len(heights) and r+i >= 0 and c+j < len(heights[0]) and c+j >= 0:
                    if (r+i,c+j) not in visited and heights[r+i][c+j] >= heights[r][c]:
                        recurse(r+i, c+j, visited)  
            return ans


        ans = []
        for r in range(len(heights)):
            recurse(r, 0, pacVisited)
            recurse(r, len(heights[0])-1, atVisited)
        
        for c in range(len(heights[0])):
            recurse(0, c, pacVisited)
            recurse(len(heights)-1, c, atVisited)
        for i in pacVisited:
            if i in atVisited:
                ans.append(i)

        
        return ans