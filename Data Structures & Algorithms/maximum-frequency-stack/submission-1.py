class FreqStack:

    def __init__(self):
        self.stack = []
        self.freq = defaultdict(int)
        self.freq_list = defaultdict(list) #{count: [count-th occurence of val]}
        self.max_freq = 0
        #{1: [5,7,4], 2:[5,7] 3: [5]}

    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.freq_list[self.freq[val]].append(val)
        self.max_freq = max(self.max_freq, self.freq[val])

    def pop(self) -> int:
        res = self.freq_list[self.max_freq].pop()
        if not self.freq_list[self.max_freq]:
            self.max_freq -= 1
        self.freq[res] -= 1
        return res

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()