class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        EMPTY = 2147483647
        queue = deque()
        rot = [(0,1), (1,0), (0,-1), (-1,0)]
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    queue.append(((i,j), 0))
        visited = set()
        while queue:
            (x,y), val = queue.popleft()
            for i,j in rot:
                if 0<=x+i<len(rooms) and 0<=y+j<len(rooms[0]) and (x+i,y+j) not in visited and rooms[x+i][y+j] == EMPTY:
                    queue.append(((x+i,y+j), val+1))
                    rooms[x+i][y+j] = val+1