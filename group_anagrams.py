class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def compareDicti(d1,d2):
            if len(d1)!=len(d2):
                return False
            for i in d1:
                if i not in d2 or d1[i]!=d2[i]:
                    return False
            
            return True
        
        dicti_list = []
        groups = []
        for word in strs:
            dicti = {}
            for c in word:
                if c in dicti:
                    dicti[c] +=1
                else:
                    dicti[c] = 1
            appended = False
            for i in range(len(groups)):
                if compareDicti(dicti, dicti_list[i]):
                    appended = True
                    groups[i].append(word)
                    break
            if not appended:
                groups.append([word])
                dicti_list.append(dicti)
        return groups