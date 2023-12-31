class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        curr = []
        def recurse(i, k):
            if k == 0:
                ans.append(list(curr))
                return
            if i > n:
                return
            recurse(i+1,k)
            curr.append(i)
            recurse(i+1,k-1)
            curr.pop()
        recurse(1, k)
        return ans

