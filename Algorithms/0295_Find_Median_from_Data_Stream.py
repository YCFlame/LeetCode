import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.hi = []  # bigger half, min heap
        self.lo = []  # smaller half, max heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.hi, num)
        temp = heapq.heappop(self.hi)
        heapq.heappush(self.lo, -temp)  # inverse to create max heap
        if len(self.hi) < len(self.lo):
            temp = heapq.heappop(self.lo)
            heapq.heappush(self.hi, -temp)

    def findMedian(self) -> float:
        return self.hi[0] if len(self.hi) > len(self.lo) else (self.hi[0] - self.lo[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
