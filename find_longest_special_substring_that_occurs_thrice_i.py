class Solution:
    def maximumLength(self, s: str) -> int:
        dicti = defaultdict(int)
        maxLen = len(s)-2
        prev = None
        for i in range(len(s)):
            if prev != None and s[prev] == s[i]:
                temp = s[i]
                # print(prev, i)
                for j in range(i-prev+1):
                    # print(temp)
                    dicti[temp]+=1
                    temp += s[i]
            else:
                prev = i
                dicti[s[i]]+=1
        
        keys = []
        for i in dicti:
            if dicti[i]>=3:
                keys.append(i)
        if not keys:
            return -1
        # print(dicti)
        # print(keys)
        return len(max(keys, key = lambda x:len(x)))
        