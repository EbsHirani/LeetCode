class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = 0
        leftDiagonal = [False]*(2*n)
        rightDiagonal = [False]*(2*n)
        vert = [False]*n

        def recurse(row):
            nonlocal ans
            if row == n:
                # print(ans)
                ans+=1
                return
            for col in range(n):
                if not (vert[col] or rightDiagonal[col+row] or leftDiagonal[row-col]):

                    vert[col] = True
                    leftDiagonal[row-col] = True
                    rightDiagonal[col+row] = True
                    
                    recurse(row+1)

                    vert[col] = False
                    leftDiagonal[row-col] = False
                    rightDiagonal[col+row] = False
        recurse(0)
        return ans