class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ans = 0
        if len(points) <= 2:
            return len(points)
        for i in range(len(points)):
            dicti = defaultdict(int)
            for j in range(len(points)):
                if i != j:
                    dicti[math.atan2(points[j][1] - points[i][1], points[j][0] - points[i][0])] += 1
            ans = max(ans, max(dicti.values())+1)
           
        
        return ans