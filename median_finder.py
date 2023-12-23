class MedianFinder:
    def __init__(self):
        self.leftHeap = []
        self.rightHeap = []

    def addNum(self, num: int) -> None:
        if self.rightHeap and self.rightHeap[0] <= num:
            heapq.heappush(self.rightHeap, num)
        else:
            heapq.heappush(self.leftHeap, -num)
        if len(self.leftHeap) > len(self.rightHeap)+1:
            temp = - heapq.heappop(self.leftHeap)
            heapq.heappush(self.rightHeap, temp)
        if len(self.rightHeap) > len(self.leftHeap):
            temp = heapq.heappop(self.rightHeap)
            heapq.heappush(self.leftHeap, -temp)

    def findMedian(self) -> float:
        if len(self.leftHeap)>len(self.rightHeap):
            return -self.leftHeap[0]
        else:
            return (self.rightHeap[0]-self.leftHeap[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()