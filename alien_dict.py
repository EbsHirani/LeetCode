class Solution:
    def alienOrder(self, words: List[str]) -> str:
        succ = {}
        pred = {}
        def word_diff(w1, w2):
            for i in range(min(len(w1), len(w2))):
                if w1[i] != w2[i]:
                    return w1[i], w2[i]
            return "", ""
        word_set = set()

        for i in range(len(words)-1):
            pre, suc = word_diff(words[i], words[i+1])
            if pre == "" and len(words[i]) > len(words[i+1]):
                return ""
            for l in words[i]:
                word_set.add(l)
            if pre in succ.keys():
                succ[pre].add(suc)
            else:
                succ[pre] = set(suc)
            if suc in pred.keys():
                pred[suc].add(pre)
            else:
                pred[suc] = set(pre)
        for l in words[-1]:
            word_set.add(l)
        ans = ""
        queue = deque()
        for l in word_set:
            if l not in pred:
                queue.append(l)
        
        while queue:
            l = queue.popleft()
            ans += l
            for i in succ.get(l, set()):
                pred[i].remove(l)
                if len(pred[i]) == 0:
                    queue.append(i)
        if len(ans) == len(word_set):
            return ans
        return ""