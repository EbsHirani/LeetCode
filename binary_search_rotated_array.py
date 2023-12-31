class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start = 0
        end = len(nums)-1

        while end>=start:
            

            mid = (start + end)//2
            if nums[start] == target or nums[end] == target or nums[mid] == target:
                return True
            while start<=end and nums[start] == nums[end]:
                start+=1
                end-=1
            if start>end:
                return False
            mid = (start + end)//2
            print(nums[start], nums[mid], nums[end])
            if nums[start] <= nums[mid]:
                print("first")
                if target > nums[mid] or target < nums[start]:
                    start = mid +1
                else:
                    end = mid -1
            else:
                print("second")
                if target<nums[mid] or target > nums[end]:
                    end = mid-1
                else:
                    start = mid+1
        return False


