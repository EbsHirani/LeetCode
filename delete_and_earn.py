class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dp = [0]*(max(nums) + 1)
        
        counts = [0]*(max(nums)+1)

        for i in nums:
            counts[i]+=1
        
        dp[1] = counts[1]

        for i in range(2, max(nums) + 1):
            dp[i] = max(dp[i-1], dp[i-2] + i*counts[i])
        return max(dp)