class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.queue = [0] * size
        self.size = size
        self.len = 0
        self.cur = 0
        self.sum = 0

    def next(self, val: int) -> float:
        self.sum += val - self.queue[self.cur]
        self.queue[self.cur] = val
        self.len = min(self.size, self.len + 1)
        self.cur = (self.cur + 1) % self.size
                
        return self.sum / self.len


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
