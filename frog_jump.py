class Solution:
    def canCross(self, stones: List[int]) -> bool:
        start = stones[0]
        target = stones[-1]
        stones = set(stones)
        visited = set()
        def recurse(i, k):
            if i not in stones:
                return False
            if i == target:
                return True
            if k<=0:
                return False
            if (i,k) in visited:
                return False
            visited.add((i,k))
            return recurse(i+k,k) or recurse(i+k-1, k-1) or recurse(i+k+1, k+1)
        return recurse(start+1,1)