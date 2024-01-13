class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        points = []
        for i, b in enumerate(buildings):
            points.append((b[0],i))
            points.append((b[1],i))

        points.sort()
        heap = []
        ans = []
        i = 0
        while i < len(points):
            point, building = points[i]

            curr = point
            # print(point)
            while i<len(points) and point == curr:
                if buildings[building][0] == curr:
                    heapq.heappush(heap, (-buildings[building][2], building))
                i+=1
                if i<len(points):
                    curr, building = points[i]

            while heap and buildings[heap[0][1]][1]<=point:
                heapq.heappop(heap)
            maxi = -heap[0][0] if heap else 0
            if not ans or ans[-1][1]!=maxi:
                ans.append((point, maxi))
        return ans
            

        
