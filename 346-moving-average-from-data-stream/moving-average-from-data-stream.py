class MovingAverage:
    # Use a queue to keep track of numbers in the queue.
    # Pop from left when the queue length is greater then k
    # Keep track of the total of the queue aswell
    def __init__(self, size: int):
        self.queue = collections.deque()
        self.size = size
        self.total = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.total += val

        if len(self.queue) > self.size:
            removed = self.queue.popleft()
            self.total -= removed
        
        return self.total / len(self.queue)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)