class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        dp = [[None]*len(dungeon[0]) for _ in range(len(dungeon))]
        def recurse(i,j):
            if i == len(dungeon)-1 and j == len(dungeon[0])-1:
                return min(dungeon[i][j],0)
            if dp[i][j]: return dp[i][j]
            ans = float("-inf")
            if i+1<len(dungeon):
                ans = min(recurse(i+1, j) + dungeon[i][j],0)
            if j+1<len(dungeon[0]):
                ans = min(max(ans, recurse(i,j+1) + dungeon[i][j]),0)
            # print(i,j, ans)
            dp[i][j] = ans
            return ans

        return 1-recurse(0,0)