class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        foundOne = False
        n = len(nums)
        for i in range(len(nums)):
            if nums[i] == 1:
                foundOne = True
            if nums[i] <=0:
                nums[i] = 1
        if not foundOne:
            return 1
        
        for i in range(len(nums)):
            # print(nums)
            if abs(nums[i])<=n:
                nums[abs(nums[i])-1] = -abs(nums[abs(nums[i])-1])
        
        for i in range(len(nums)):
            if nums[i]>0:
                return i+1
        return len(nums)+1