class TimeMap:

    def __init__(self):
        self.m = defaultdict(list)

        #{alice: [(happy, 1), (happy, 2), (sad, 4)]}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.m[key]) - 1
        entries = self.m[key]

        while l <= r:
            m = (l + r) // 2
            val, t = entries[m]

            if t == timestamp:
                return val
            elif t < timestamp:
                l = m + 1
            else:
                r = m - 1
        
        return entries[r][0] if r >= 0 else ""
        
