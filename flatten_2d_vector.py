class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.curr_row = 0
        self.curr_col = 0
        while self.curr_row < len(self.vec) and not self.vec[self.curr_row]:
            self.curr_row+=1 

    def next(self) -> int:
        print(self.curr_row, self.curr_col)
        
        ans= self.vec[self.curr_row][self.curr_col]
        if len(self.vec[self.curr_row])>self.curr_col+1:
            self.curr_col += 1
            
        else:
            self.curr_row+=1
            self.curr_col = 0
            while self.curr_row < len(self.vec) and not self.vec[self.curr_row]:
                self.curr_row+=1                
        return ans

    def hasNext(self) -> bool:
        return self.curr_row<len(self.vec) and self.vec[self.curr_row]
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()