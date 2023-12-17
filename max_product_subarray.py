class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        maxNprod = min(nums[0],0)
        maxPprod = max(nums[0],0)
        ans = maxPprod
        for i in range(1, len(nums)):
            if nums[i]>0:
                maxPprod = max(maxPprod*nums[i], nums[i])
                maxNprod = maxNprod*nums[i]
            else:
                maxPprodTemp = maxNprod*nums[i] 
                maxNprod = min(maxPprod*nums[i], nums[i])
                maxPprod = maxPprodTemp
            ans = max(ans, maxPprod)
        
        return ans