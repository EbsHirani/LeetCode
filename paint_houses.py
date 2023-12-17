class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp = [[0]*3 for _ in range(2)]
        dp[0] = costs[0]
        dp[1] = list(dp[0])
        for i in range(1, len(costs)):
            dp[1][0] = costs[i][0] + min(dp[0][1], dp[0][2])
            dp[1][1] = costs[i][1] + min(dp[0][0], dp[0][2])
            dp[1][2] = costs[i][2] + min(dp[0][1], dp[0][0])

            dp[0] = list(dp[1])
        return min(dp[-1])