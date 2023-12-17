class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float("inf")] * len(nums)
        dp[-1] = 0
        for i in reversed(range(len(nums)-1)):
            print(i+1, min(len(nums), i+nums[i]))
            for j in range(i+1, min(len(nums), 1+i+nums[i])):
                
                dp[i] = min(dp[i], 1+dp[j])
        return dp[0]