class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.size = size
        self.cur = 0

    def next(self, val: int) -> float:
        if len(self.queue) < self.size:
            self.queue.append(val)
        else:
            self.queue[self.cur] = val
            self.cur = (self.cur + 1) % self.size
                
        return sum(self.queue) / len(self.queue)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
