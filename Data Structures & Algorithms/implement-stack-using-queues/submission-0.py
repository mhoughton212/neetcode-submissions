class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        self.queue.reverse()
        top = self.queue.popleft()
        self.queue.reverse()
        return top
        
    def top(self) -> int:
        self.queue.reverse()
        top = self.queue[0]
        self.queue.reverse()
        return top

    def empty(self) -> bool:
        return len(self.queue) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()