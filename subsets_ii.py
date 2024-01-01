class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        dicti = defaultdict(int)
        for i in nums:
            dicti[i] += 1
        
        ans = []
        curr = []
        keys = list(dicti.keys())
        def recurse(i):
            nonlocal curr
            if i>=len(keys):
                ans.append(list(curr))
                return
            recurse(i+1)
            prev = list(curr)
            for j in range(dicti[keys[i]]):
                curr.append(keys[i])
                recurse(i+1)
            curr = prev

        
        recurse(0)
        return ans