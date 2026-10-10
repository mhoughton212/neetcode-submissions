class ListNode:
    def __init__(self, key = None, val = None):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.hashmap = [ListNode() for i in range(10_000)]

    def put(self, key: int, value: int) -> None:
        curr = self.hashmap[key % len(self.hashmap)]
        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            curr = curr.next
        curr.next = ListNode(key, value)
        return
        

    def get(self, key: int) -> int:
        curr = self.hashmap[key % len(self.hashmap)]
        while curr.next:
            if curr.next.key == key:
                return curr.next.val
            curr = curr.next
        return -1
        

    def remove(self, key: int) -> None:
        curr = self.hashmap[key % len(self.hashmap)]
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next
        return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)