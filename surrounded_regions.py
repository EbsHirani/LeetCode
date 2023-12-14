class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        untouchable = set()
        def checkBorderOs(x,y):
            if (x,y) in untouchable:
                return
            untouchable.add((x,y))
            if x-1>=0 and board[x-1][y]=="O":
                checkBorderOs(x-1,y)
            if x+1<rows and board[x+1][y]=="O":
                checkBorderOs(x+1,y)
            if y-1>=0 and board[x][y-1]=="O":
                checkBorderOs(x,y-1)
            if y+1<cols and board[x][y+1]=="O":
                checkBorderOs(x,y+1)
            return
        
        for i in range(rows):
            if board[i][0] == "O":
                checkBorderOs(i,0)
            if board[i][cols-1] == "O":
                checkBorderOs(i,cols-1)
        for i in range(cols):
            if board[0][i] == "O":
                checkBorderOs(0,i)
            if board[rows-1][i]=="O":
                checkBorderOs(rows-1,i)
        print(untouchable)  
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O" and (i,j) not in untouchable:
                    board[i][j] = "X"
        return board
                