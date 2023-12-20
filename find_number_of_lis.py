class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [None]*len(nums)
        dp[0] = (1,1)
        global_max = 1
        def recurse(n):
            print(n)
            nonlocal global_max
            
            if dp[n] != None:
                return dp[n]
            
            maxi,maxcount = 0,1
            for i in range(n):
                if nums[i]<nums[n]:
                    seq_size,count = recurse(i)
                    if seq_size>maxi:
                        maxi, maxcount = seq_size,count
                    elif seq_size==maxi:
                        maxcount+=count
            dp[n] = (maxi+1, maxcount)
            global_max = max(maxi+1, global_max)
            return maxi, maxcount
        for i in range(len(nums)):
            recurse(i)
        ans = 0
        print(dp)
        for i in dp:
            if i[0] == global_max:
                ans+=i[1]
        
        return ans
