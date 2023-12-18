class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = [[-1]*len(nums) for _ in range(len(nums))]
        def recurse(i,j):
            if j<i:
                return 0
            if i==j:
                ans = nums[i]
                if i-1>=0:
                    ans*=nums[i-1]
                if i+1<len(nums):
                    ans*=nums[i+1]
                return ans
            if dp[i][j]!=-1: return dp[i][j]
            ans = 0
            temp = 1
            if i-1>=0:
                temp*=nums[i-1]
            if j+1<len(nums):
                temp*=nums[j+1]
            for x in range(i,j+1):
                ans = max(nums[x]*temp + recurse(i,x-1)+recurse(x+1,j), ans)
            dp[i][j] = ans
            return ans
        
        return recurse(0,len(nums)-1)