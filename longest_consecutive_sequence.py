class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        ans = 0
        for i in nums:
            if i-1 not in numset:
                j = i+1
                temp = 1
                while j in numset:
                    temp+=1
                    j+=1
                ans = max(ans, temp)
        
        return ans
        
        