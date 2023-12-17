class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}
        if len(s3) != len(s1)+len(s2):
            return False
        def recurse(i,j,k):
            if (i,j,k) in dp:
                return dp[(i,j,k)]
            if k>=len(s3):
                return True
            if i<len(s1) and s1[i] == s3[k] and recurse(i+1,j,k+1):
                return True
            if j<len(s2) and s2[j] == s3[k] and recurse(i,j+1,k+1):
                return True
            dp[(i,j,k)] = False
            return False
        return recurse(0,0,0)