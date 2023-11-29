class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        included = set()
        currSum = 0
        nums.sort()
        if sum(nums)%k!=0:
            return False
        
        targetSum = sum(nums)//k
        if max(nums) > targetSum:
            return False
        def backtrack(id, currSum, targetSum):
            if currSum == 0:
                id = 0
            if len(included) == len(nums):
                return True
            
            for i in range(id, len(nums)):
                if i not in included:
                    if currSum + nums[i] > targetSum:
                        break
                        
                    included.add(i)
                    if backtrack(i+1, (currSum + nums[i])%targetSum, targetSum):
                        return True
                    included.remove(i)
            return False
        for i in range(len(nums)):
            if nums[i] == targetSum:
                included.add(i)
        return backtrack(0,0, targetSum)

            