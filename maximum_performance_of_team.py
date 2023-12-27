class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        index = sorted(range(n), key = lambda x: efficiency[x], reverse = True)
        ans = float("-inf")
        total = 0
        MOD = 1000000007
        minheap = []
        
        for i in index:
            if len(minheap)==k:
                total-=heapq.heappop(minheap)
            total = total + speed[i]
            heapq.heappush(minheap, speed[i])
            ans = max(total*efficiency[i], ans)

        return ans%MOD
