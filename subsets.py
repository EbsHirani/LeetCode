class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        curr = []

        def recurse(i):
            if i==len(nums):
                ans.append(list(curr))
                return
            recurse(i+1)
            curr.append(nums[i])
            recurse(i+1)
            curr.pop()
        
        recurse(0)
        return ans