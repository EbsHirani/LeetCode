class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] != None and matrix[i][j] == 0:
                    print(i,j)
                    for k in range(len(matrix)):
                        if matrix[k][j] and matrix[k][j] !=0:
                            print("hi")
                            matrix[k][j] = None
                    for k in range(len(matrix[0])):
                        if matrix[i][k] and matrix[i][k] !=0:
                            print("hi")
                            matrix[i][k] = None
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if not matrix[i][j]:
                    matrix[i][j] = 0