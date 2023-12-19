class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 != 0:
            return False
        target = sum(nums)//2
        dp = [[False]*(target+1) for _ in range(len(nums))]

        for i in range(len(nums)):
            dp[i][0] = True
        
        for i in range(len(nums)):
            for j in range(1, target+1):
                if j-nums[i]>=0:
                    dp[i][j] = dp[i-1][j-nums[i]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[-1][-1]