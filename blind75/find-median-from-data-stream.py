class MedianFinder:

    def __init__(self):
        self.midleft = [] # max heap
        self.midright = [] # min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.midleft, -1 * num)
        
        if self.midleft and self.midright and (-1 * self.midleft[0]) > self.midright[0]:
            val = -1 * heapq.heappop(self.midleft)
            heapq.heappush(self.midright, val)

        if len(self.midleft) > len(self.midright) + 1:
            val = -1 * heapq.heappop(self.midleft)
            heapq.heappush(self.midright, val)

        if len(self.midright) > len(self.midleft) + 1:
            val = heapq.heappop(self.midright)
            heapq.heappush(self.midleft, -1 * val)

    def findMedian(self) -> float:
        if len(self.midleft) > len(self.midright):
            return -1 * self.midleft[0]
        elif len(self.midright) > len(self.midleft):
            return self.midright[0]
            
        return (-1 * self.midleft[0] + self.midright[0]) / 2
        
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()