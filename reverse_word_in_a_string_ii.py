class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        for i in range(len(s)//2):
            
            s[i], s[len(s)-1 -i] = s[len(s)-1 -i], s[i]

        i = 0
        # print(s)
        while i<len(s):
            if s[i] == " ":
                i+=1
                continue
            end = i
            while end+1<len(s) and s[end+1]!=" ":
                end+=1
            # print(i,end)
            
            for j in range(i, (i+end+1)//2):
                s[j], s[i+end-j] = s[i+end-j],s[j]
            i = end+1