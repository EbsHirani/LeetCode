class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] or obstacleGrid[0][0]:
            return 0
        obstacleGrid[0][0] = 1
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] and (i!=0 or j!=0):
                    obstacleGrid[i][j] = 0
                    continue

                if i>0:
                    obstacleGrid[i][j] += obstacleGrid[i-1][j]
                if j>0:
                    obstacleGrid[i][j] += obstacleGrid[i][j-1]
        print(obstacleGrid)
        return obstacleGrid[-1][-1] 