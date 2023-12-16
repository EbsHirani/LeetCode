class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        ans = set()
        notans = set()
        visited = set()
        def dfs(i):
            if i in ans:
                return True
            if len(graph[i]) == 0:
                ans.add(i)
                return True
            visited.add(i)
            for j in graph[i]:
                if j in visited or not dfs(j):
                    notans.add(i)
                    return False
            visited.remove(i)
            ans.add(i)
            return True

        for i in range(len(graph)):
            if i not in ans and i not in notans:
                dfs(i)
        return sorted(list(ans))
