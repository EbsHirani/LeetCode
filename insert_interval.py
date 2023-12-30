class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        toMerge = set()
        for i in range(len(intervals)):
            interval = intervals[i]
            if interval[0]<=newInterval[1] and newInterval[0]<=interval[1]:
                toMerge.add(i)
        
        start = newInterval[0]
        end = newInterval[1]
        for i in toMerge:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
        ans = []
        isInserted = False
        for i in range(len(intervals)):
            if not isInserted and intervals[i][0]>end:
                ans.append((start,end))
                isInserted = True
            if i not in toMerge:
                ans.append(intervals[i])

        if not isInserted:
            ans.append((start,end))

        return ans
            