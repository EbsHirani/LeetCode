class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        checkGreat = True

        for i in range(len(nums)-1):
            if checkGreat:
                if nums[i]>nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
            else:
                if nums[i]<nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
            checkGreat = not checkGreat