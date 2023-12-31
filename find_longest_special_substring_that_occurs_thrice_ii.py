class Solution:
    def maximumLength(self, s: str) -> int:
        dicti = defaultdict(int)
        maxLen = len(s)-2
        curr = 0
        
        while curr< len(s):
            nex = curr
            while nex<len(s) and s[curr] == s[nex]:
                nex+=1
            numChars = nex - curr
            for i in range(max(numChars-2,1),numChars+1):
                dicti[s[curr]*i] += numChars - i + 1
            curr = nex
                
        
        keys = []
        for i in dicti:
            if dicti[i]>=3:
                keys.append(i)
        if not keys:
            return -1
        print(dicti)
        # print(keys)
        return len(max(keys, key = lambda x:len(x)))