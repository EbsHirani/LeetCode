class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1]*n
        def find(i):
            while parent[i] != i:
                parent[i] = parent[parent[i]]
                i = parent[i]
            return i
        
        def union(i,j):
            p_i = find(i)
            p_j = find(j)
            if p_i == p_j:
                return False
            
            if rank[p_i]>=rank[p_j]:
                parent[p_j] = p_i
                rank[p_i] += rank[p_j]
            else:
                parent[p_i] = p_j
                rank[p_j] += rank[p_i]
            return True
        
        for i,j in edges:
            union(i,j)
        
        count = 0
        for i in range(len(parent)):
            if parent[i] == i:
                count+=1
        return count