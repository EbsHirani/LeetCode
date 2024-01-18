class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # for i in board:
        #     print(i)
        nbrs = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                nbCount = 0
                for x,y in nbrs:
                    if 0<=i+x<len(board) and 0<=j+y<len(board[0]):
                        if board[i+x][j+y]>=1:
                            nbCount+=1
                if board[i][j] == 1:
                    if nbCount<2 or nbCount>3:
                        board[i][j] = 2
                if board[i][j] == 0 and nbCount == 3:
                    board[i][j] = -1
        # print("==")
        # for i in board:
        #     print(i)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == -1:
                    board[i][j] = 1
        # print("==")
        # for i in board:
        #     print(i)
        

        