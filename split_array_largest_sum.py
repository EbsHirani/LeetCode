class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        dp = [[None]*(k+1) for _ in range(len(nums))]

        def recurse(i,k):
            if k == 1:
                return sum(nums[:i+1])
            if k==i+1:
                return max(nums[:i+1])
            if k>i+1:
                return float("inf")
            if dp[i][k] != None:
                return dp[i][k]
            ans = float("inf")
            tot = nums[i]
            for id in reversed(range(k-2,i)):
                ans = min(ans, max(recurse(id, k-1), tot))
                tot+=nums[id]
                if tot>= ans:
                    break
            dp[i][k] = ans
            return ans

        ans = recurse(len(nums)-1, k)
        return ans