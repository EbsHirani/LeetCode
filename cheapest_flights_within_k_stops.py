class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        shortest = {}
        graph = {i:[] for i in range(n)}
        for fr, to, p in flights:
            graph[fr].append((to,p))
        val = [float("inf")]*n
        prev = [float("inf")]*n
        prev[src] = val[src] = 0

        for _ in range(k+1):
            for node in range(n):
                if prev[node] != float("inf"):
                    for nbr, p in graph[node]:
                        if prev[nbr] > prev[node] + p:
                            val[nbr] = min(prev[node] + p, val[nbr])
            prev = list(val)
        
        if val[dst] != float("inf"):
            return val[dst]
        return -1