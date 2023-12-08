class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        dp = [[0]*len(dist) for _ in range(len(dist))]
        dp[0][0] = dist[0]
        for i in range(1,len(dist)):
            diff = 0 if dp[0][i-1]%speed == 0 else speed - dp[0][i-1]%speed
            dp[0][i] = dp[0][i-1] + diff  + dist[i]  
            dp[i][0] = dp[0][0]
        
        if dp[0][-1] <= hoursBefore*speed:
            # print(dp)
            return 0

        for row in range(1, len(dist)):
            for col in range(1, len(dist)):
                diff = 0 if dp[row][col-1]%speed == 0 else speed - dp[row][col-1]%speed           
                dp[row][col] = min(dp[row-1][col-1] + dist[col], dp[row][col-1] + diff + dist[col])
            if dp[row][-1] <= hoursBefore*speed:
                # print(dp)
                return row

        return -1


