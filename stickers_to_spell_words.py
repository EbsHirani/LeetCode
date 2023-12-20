#1 BRUTE FORCE TLE APPROACH:
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        target_dicti = {}
        for i in target:
            if i in target_dicti:
                target_dicti[i]+=1
            else:
                target_dicti[i] = 1
        word_dicti = []
        for word in stickers:
            dicti = {}
            for i in word:
                if i in target:
                    if i in dicti:
                        dicti[i] += 1
                    else:
                        dicti[i] = 1
            word_dicti.append(dicti)
        unsatisfied = set(target_dicti.keys())
        print(unsatisfied)
        def recurse(i):
            nonlocal unsatisfied
            if len(unsatisfied) == 0:
                return 0
            elif i>=len(word_dicti):
                return -1
            temp = recurse(i+1)
            if temp == -1:
                ans = float("inf")
            else:
                ans = temp
            dicti = word_dicti[i]
            removal_set = set()
            updated = False
            for c in unsatisfied:
                if c in dicti:
                    updated = True
                    target_dicti[c] -= dicti[c]
                    if target_dicti[c]<=0:
                        removal_set.add(c)
            
            if updated:
                unsatisfied = unsatisfied.difference(removal_set)
                temp = recurse(i)
                if temp!=-1:
                    ans = min(ans, temp+1)
                unsatisfied = unsatisfied.union(removal_set)
                for c in unsatisfied:
                    if c in dicti:
                        target_dicti[c] += dicti[c]
            if ans == float("inf"):
                return -1
            return ans

            

        return recurse(0)
    
#2 MEMOIZATION APPROACH:

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        word_dicti = []
        for word in stickers:
            dicti = {}
            for i in word:
                if i in target:
                    if i in dicti:
                        dicti[i] += 1
                    else:
                        dicti[i] = 1
            word_dicti.append(dicti)
        dp = {}
        def recurse(target):
            # print(target)
            if target in dp:
                return dp[target]
            if target == "":
                return 0
            ans = float("inf")

            for word in word_dicti:
                newDicti = dict(word)
                newString = ""
                check = False
                for c in target:
                    if c in newDicti and newDicti[c]>0:
                        check = True
                        newDicti[c]-=1
                    else:
                        newString += c
                if check:
                    ans = min(ans, recurse(newString) + 1)
            dp[target] = ans
            return ans
        ans = recurse(target)
        if ans != float("inf"):
            return ans
        return -1
