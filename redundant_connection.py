class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {i:i for i in range(1, len(edges)+1)}
        def find(i):
            if parent[i] == i:
                return i
            else:
                parent[i] = find(parent[i])
                return parent[i]
        def union(i,j):
            p_i = find(i)
            p_j = find(j)
            parent[p_i] = p_j
        
        ans = None
        for i,j in edges:
            p_i = find(i)
            p_j = find(j)
            if p_i == p_j:
                ans = [i,j]
            else:
                union(i,j)
        
        return ans
