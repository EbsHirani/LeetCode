#Split select a point, only need to search in top right and bottom left
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
            
        def recurse(left, right, up, down):
            # print(left,right,up,down)
            if left>right or up>down:
                return False
            row = (down+up)//2
            left_, right_ = left, right
            div_col = left_
            while left_<=right_:
                mid = (left_+right_)//2
                if matrix[row][mid] == target:
                    return True
                if matrix[row][mid] <target:
                    div_col = mid
                    left_ = mid+1
                else:
                    right_ = mid-1
            # print("dividing at:",row, div_col, matrix[row][div_col])
            return recurse(left, div_col, row+1, down) or recurse(div_col,right, up, row-1)
        # for i in matrix:
        #     print(i)
        # print("____")
        return recurse(0,len(matrix[0])-1,0, len(matrix)-1)