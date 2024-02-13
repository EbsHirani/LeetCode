class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        graph = defaultdict(list)

        if target == source:
            return 0

        for i in range(len(routes)):
            routes[i] = set(routes[i])
        
        for i in range(len(routes)):
            for j in range(i+1, len(routes)):
                if len(routes[i].intersection(routes[j])) > 0:
                    graph[i].append(j)
                    graph[j].append(i)
        queue = deque([])
        visited = set()
        for bus in range(len(routes)):
            if source in routes[bus]:
                queue.append((bus, 1))
                visited.add(bus)

        while queue:
            bus, dist = queue.popleft()
            
            if target in routes[bus]:

                return dist

            for i in graph[bus]:
                if i not in visited:
                    queue.append((i,dist+1))
                    visited.add(i)
        print(visited)

        return -1