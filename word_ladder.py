class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int: 
        wordList.append(beginWord)
        templateDict = {}
        for i in range(len(wordList)):
            for c in range(1,len(wordList[i])+1):
                template = wordList[i][:c-1] + "*" + wordList[i][c:]
                if template in templateDict:
                    templateDict[template].append(wordList[i])
                else:
                    templateDict[template] = [wordList[i]]

        visited = set(beginWord)

        queue = deque()
        queue.append((beginWord,1))

        while queue:
            # print(queue)
            word, steps = queue.popleft()
            for c in range(1, len(word)+1):
                template = word[:c-1] + "*" + word[c:]
                for adj in templateDict[template]:
                    if adj == endWord:
                        return steps+1
                    if adj not in visited:
                        queue.append((adj, steps + 1))
                        visited.add(adj)

        return 0