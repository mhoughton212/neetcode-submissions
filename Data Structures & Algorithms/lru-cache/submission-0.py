class ListNode:
    def __init__(self, key: int = 0, val: int = 0, prev: "Node" = None, next: "Node" = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = ListNode()
        self.tail = ListNode()

        self.head.next = self.tail
        self.tail.prev = self.head
    
    def insert(self, node):
        prev = self.tail.prev

        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node
    
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val 

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insert(node)
        else:
            node = ListNode(key, value)
            self.cache[key] = node
            self.insert(node)
            if len(self.cache) > self.capacity:
                lru = self.head.next
                self.remove(lru)
                del self.cache[lru.key]




        
