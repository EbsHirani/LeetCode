class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        dicti = defaultdict(int)
        for i in nums:
            dicti[i] += 1

        ans = []
        temp = []
        def recurse():
            if len(temp) == len(nums):
                ans.append(list(temp))
                return
            
            for i in dicti.keys():
                if dicti[i]>0:
                    temp.append(i)
                    dicti[i] -= 1
                    recurse()
                    dicti[i] += 1
                    temp.pop()
        
        recurse()
        return ans

