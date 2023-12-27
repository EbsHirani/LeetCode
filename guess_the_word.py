# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        
        def common(w1, w2):
            count = 0
            for c1,c2 in zip(w1, w2):
                if c1==c2:
                    count+=1
            return count
        commonArr = [[0]*len(words) for _ in words]
        
        for i in range(len(words)):
            for j in range(len(words)):
                commonArr[i][j] = common(words[i], words[j])

        wordSet = set(range(len(words)))
        
        while True:
            word = None
            common = 0
            for i in range(len(words)):
                temp = 0
                if i in wordSet:
                    for j in range(len(words)):
                        if j in wordSet:
                            temp+= commonArr[i][j]
                    
                    if temp>common:
                        common = temp
                        word = i
            ans = master.guess(words[word])
            print(words[word], ans)
            if ans == 6:
                return
            for i in range(len(words)):
                if i in wordSet and commonArr[word][i] != ans:
                    wordSet.remove(i)