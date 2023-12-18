class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        dicti = {}
        for i in candidates:
            if i in dicti:
                dicti[i]+=1
            else:
                dicti[i] = 1
        keyList = list(dicti.keys())
        ans = []
        temp = []
        def recurse(i,t):
            if t==0:
                ans.append(list(temp))
                return
            if i>=len(keyList) or t<0:
                return 
            recurse(i+1, t)
            if dicti[keyList[i]] !=0:
                dicti[keyList[i]]-=1
                temp.append(keyList[i])
                recurse(i,t-keyList[i])
                temp.pop()
                dicti[keyList[i]]+=1
            return 
        recurse(0,target)
        return ans