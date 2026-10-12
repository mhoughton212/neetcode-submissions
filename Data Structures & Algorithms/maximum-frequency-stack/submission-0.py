class FreqStack:

    def __init__(self):
        self.stack = []
        self.freq = defaultdict(int)


    def push(self, val: int) -> None:
        self.stack.append(val)
        self.freq[val] += 1

    def pop(self) -> int:
        most_freq = max(self.freq.values())
        for i in range(len(self.stack) - 1, -1, -1):
            val = self.stack[i]
            if self.freq[val] == most_freq:
                self.stack.pop(i)
                self.freq[val] -= 1
                return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()