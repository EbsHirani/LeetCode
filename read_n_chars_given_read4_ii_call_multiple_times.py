# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.prev = []
    def read(self, buf: List[str], n: int) -> int:
        btsread = 0
        if self.prev:
            while btsread<len(self.prev) and btsread<n:
                buf[btsread] = self.prev[btsread]
                btsread+=1
            self.prev = self.prev[btsread:]
        tempbuf = ['']*4
        br = False
        while btsread < n:
            k = read4(tempbuf)
            for i in range(k):
                if btsread>=n:
                    self.prev = tempbuf[i:k]
                    break
                buf[btsread]=tempbuf[i]
                btsread+=1      
            if k<4:
                break
        return btsread