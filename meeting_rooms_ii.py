def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        maxOverlaps = 0
        for i in range(len(intervals)):
            time = intervals[i][1]
            overlaps = 0
            for j in range(len(intervals)):
                if intervals[j][0] < time <= intervals[j][1]:
                    overlaps +=1
            
            maxOverlaps = max(maxOverlaps, overlaps)

        return maxOverlaps

#Alternative:

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        
        roomNum = 0
        currRoom = None
        while intervals:
            tempList = []
            roomNum+=1
            for i in range(len(intervals)):
                interval = intervals[i]
                if currRoom:
                    lastInterval = currRoom
                    if lastInterval[0]<=interval[1] and lastInterval[1]>interval[0]:
                        tempList.append(intervals[i])
                        continue
                currRoom = intervals[i]
                
            intervals = tempList
            currRoom = None
        
        return roomNum
