class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        pred = {i: set() for i in range(n)}
        succ = {i:set() for i in range(n)}
        for s, d in connections:
            pred[d].add(s)
            succ[s].add(d)
        
        visited = set([0])
        queue = deque()
        queue.append(0)
        count = 0
        while queue:
            node = queue.popleft()
            for pre in pred[node]:
                if pre not in visited:
                    visited.add(pre)
                    queue.append(pre)
            
            for suc in succ[node]:
                if suc not in visited:
                    visited.add(suc)
                    count+=1
                    queue.append(suc)
        
        return count