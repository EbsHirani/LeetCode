class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s)-len(t))>1:
            return False
        if len(s) == 0 or len(t) == 0:
            return abs(len(s)-len(t)) == 1
        
        for i in range(min(len(s), len(t))):
            if s[i] != t[i]:
                if len(s) == len(t):
                    return s[i+1:] == t[i+1:]
                elif len(s)>len(t):
                    return s[i+1:] == t[i:]
                else:
                    return s[i:] == t[i+1:]


        return abs(len(s)-len(t)) == 1