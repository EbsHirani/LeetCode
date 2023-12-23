class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        ans = []
        curr = 1
        currInterval = intervals[0]

        while curr < len(intervals):
            it = intervals[curr]
            if it[0] > currInterval[1]:
                ans.append(currInterval)
                currInterval = it
            else:
                currInterval[1] = max(currInterval[1], it[1])
            curr+=1
        
        ans.append(currInterval)

        return ans