class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList.append(beginWord)
        dicti = defaultdict(list)
        wordList = set(wordList)
        
        visited = set([beginWord])
        currLevel = set()
        queue = [beginWord]
        found = False
        while (not found) and queue:
            nextSet = set()
            while queue:
                word = queue.pop()
                if word == endWord:
                    found = True
                    break
                for i in range(1, len(word) + 1):
                    for c in list(map(chr,range(ord('a'),ord('z')+1))):
                        temp = word[:i-1] + c + word[i:]
                        if temp in wordList:
                            if temp not in visited:
                                nextSet.add(temp)
                                dicti[temp].append(word)
            visited = visited.union(nextSet)
            queue = list(nextSet)
        
        if not found:
            return []

        ans = []
        curr = [endWord]
        
        def recurse(word):
            nonlocal ans
            if word == beginWord:
                ans.append(curr[::-1])
                return
            
            for nbr in dicti[word]:
                
                curr.append(nbr)
                recurse(nbr)
                curr.pop()

        recurse(endWord)
        return ans