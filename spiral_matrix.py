class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        currDir = 0
        ans = []
        visited = [[0]*len(matrix[0]) for _ in range(len(matrix))]
        x,y = 0,0
        while True:
            ans.append(matrix[x][y])
            visited[x][y] = 1
            i,j = directions[currDir]
            if x+i<0 or x+i>=len(matrix) or y+j<0 or y+j>=len(matrix[0]) or visited[x+i][y+j]:
                currDir = (currDir+1)%4
                i,j = directions[currDir]
                if x+i<0 or x+i>=len(matrix) or y+j<0 or y+j>=len(matrix[0]) or visited[x+i][y+j]:
                    return ans
            x+=i
            y+=j