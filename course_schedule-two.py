class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        successors = {i:set() for i in range(numCourses)}
        pred = {i:set() for i in range(numCourses)}
        for succ, pre in prerequisites:
            successors[pre].add(succ)
            pred[succ].add(pre)

        ans = []
        queue = deque()
        for i in pred:
            if len(pred[i]) == 0:
                queue.append(i)
        while queue:
            curr = queue.popleft()
            ans.append(curr)
            for i in successors[curr]:
                pred[i].remove(curr)
                if len(pred[i]) == 0:
                    queue.append(i)
        
        if len(ans)< numCourses:
            return []
        
        return ans