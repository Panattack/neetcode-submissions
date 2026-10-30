class MovingAverage:

    def __init__(self, size: int):
        self.sum = 0
        self.queue = deque()
        self.size = size

    def next(self, val: int) -> float:
        if len(self.queue) < self.size:
            self.sum += val
            self.queue.append(val)
        else:
            old = self.queue.popleft()
            self.queue.append(val)
            self.sum -= old
            self.sum += val

        return self.sum / len(self.queue)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
