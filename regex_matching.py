class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dicti = {}
        def recurse(i,j):
            if i>=len(s) and j>=len(p):
                return True
            if (i,j) in dicti:
                return dicti[(i,j)]   
            ans = False
            if j+1<len(p) and p[j+1] == "*":
                ans = ans or recurse(i,j+2)
                if i<len(s) and (s[i] == p[j] or p[j] =="."):
                    ans = ans or recurse(i+1,j) or recurse(i+1, j+2)
            elif i<len(s) and j<len(p) and (s[i] == p[j] or p[j] =="."):
                ans = recurse(i+1,j+1)
            dicti[(i,j)] = ans
            return ans 
        ans = recurse(0,0)
        return ans