class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        count = 0
        for i in nums:
            if i%2 ==0:
                count+=1
        return count>= 2