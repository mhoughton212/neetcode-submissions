class MyHashSet:

    def __init__(self):
        self.container = [False] * 1_000_000

    def add(self, key: int) -> None:
        i = hash(key % len(self.container))
        self.container[i] = True
        return None
        

    def remove(self, key: int) -> None:
        i = hash(key % len(self.container))
        self.container[i] = False
        return None

    def contains(self, key: int) -> bool:
        return self.container[hash(key) % len(self.container)]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)