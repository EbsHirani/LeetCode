class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        curr = 0
        ans = []
        while curr<len(words):
            s = ""
            space = maxWidth
            temp = curr
            while temp < len(words) and space >= len(words[temp]):
                space -= len(words[temp]) + 1
                temp+=1
            numWords = temp-curr
            space+=1
            if numWords == 1:
                s += words[curr] + " "*(space)
            elif temp >= len(words):
                for i in range(curr, temp-1):
                    s += words[i] + " "     
                print(space)  
                s+=words[temp-1] + " "*space
            else:
                div = space//(numWords-1)
                extra = space%(numWords-1)
                for i in range(curr, temp-1):
                    s += words[i] + " "*(div+1)
                    if extra:
                        s += " "
                        extra-=1
                s+=words[temp-1]
            # print(s, numWords, space)
            ans.append(s)
            curr = temp
        return ans