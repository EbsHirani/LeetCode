class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        boardMap = [0]*(n*n)
        for i in range(n):
            for j in range(n):
                if (n-i-1)%2 == 0:
                    boardMap[(n-i-1)*n + j] = (i,j)
                else:
                    boardMap[(n-i-1)*n + (n-j-1)] = (i,j)
        def getBoardVal(x):
            i, j = boardMap[x]
            return board[i][j] - 1
        queue = deque()
        visited = set()
        queue.append((0,0))
        visited.add(0)
        # print(boardMap)
        while queue:
            x, steps = queue.popleft()
            for y in range(x+1, min(x+7, n*n)):
                val = getBoardVal(y) 
                val = y if val == -2 else val
                # print(val)
                if val == n*n-1:
                    return steps+1
                elif val not in visited:
                    visited.add(val)
                    queue.append((val, steps+1))

        return -1