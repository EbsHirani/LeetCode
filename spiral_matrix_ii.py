class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        currDir = 0
        ans = [[0]*n for _ in range(n)]
        x,y = 0,0
        count = 1
        while True:
            ans[x][y] = count
            count+=1
            i,j = directions[currDir]
            if x+i<0 or x+i>=len(ans) or y+j<0 or y+j>=len(ans[0]) or ans[x+i][y+j]:
                currDir = (currDir+1)%4
                i,j = directions[currDir]
                if x+i<0 or x+i>=len(ans) or y+j<0 or y+j>=len(ans[0]) or ans[x+i][y+j]:
                    return ans
            x+=i
            y+=j