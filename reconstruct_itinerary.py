class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(lambda:[])
        notvisited = {}
        # remaining = defauldict(lambda:0)
        # elSet = set()
        rem = 0
        ans = ["JFK"]
        def solve(key):
            nonlocal rem, ans, graph,notvisited
            if rem==0:
                return True
            
            # if rem <3:
            #     print(ans)
            #     print(notvisited)
            #     print("***************")
            
            for i in range(len(graph[key])):
                if graph[key][i] in notvisited[key]:
                    ans.append(graph[key][i])
                    
                    del graph[key][i]
                    rem-=1
                    if solve(ans[-1]):
                        return True

                    rem+=1
                    graph[key].insert(i,ans.pop())
            return False
                 
                
                
        
        for key, val in tickets:
            graph[key].append(val)
            # remaining[key]+=1
            rem+=1
            # elSet.add(key)
            # elSet.add(val)
        for key in graph:
            graph[key] = sorted(graph[key])
            notvisited[key] = list(graph[key])
        
        keys = list(graph.keys()) 
        
        solve("JFK")
        return ans