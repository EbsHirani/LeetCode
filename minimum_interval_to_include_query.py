class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        ans = [-1]*len(queries)
        queryId = sorted(range(len(queries)), key=lambda x: queries[x])
        
        currInterval = 0

        minHeap = []
        for q in queryId:

            query = queries[q]
            while currInterval < len(intervals) and intervals[currInterval][0]<=query:
                heapq.heappush(minHeap, (intervals[currInterval][1] - intervals[currInterval][0] + 1, intervals[currInterval][1]))
                currInterval+=1
                
            while minHeap and minHeap[0][1]<query:
                heapq.heappop(minHeap)

            if minHeap:
                ans[q] = minHeap[0][0]
        return ans
            
