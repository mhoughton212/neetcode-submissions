class ListNode:
    def __init__(self, key: int = 0, val: int = 0, prev: "ListNode" = None, next: "ListNode" = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next, self.tail.prev = self.tail, self.head
        self.size = 0

    def insert(self, node):
        prev = self.tail.prev
        prev.next, node.prev = node, prev
        node.next, self.tail.prev = self.tail, node
        self.size += 1

    def pop(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
        self.size -= 1
    
    def popLeft(self):
        if not self.size:
            return
        node = self.head.next
        self.pop(node)
        return node
        
class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.list_frequencies = defaultdict(LinkedList)
        self.key_uses = {}
        self.node_map = {}
        self.lfu_count = 0

    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1

        count = self.key_uses[key]
        node = self.node_map[key]

        self.list_frequencies[count].pop(node)
        self.list_frequencies[count + 1].insert(node)

        self.key_uses[key] += 1

        if count == self.lfu_count and not self.list_frequencies[count].size:
            self.lfu_count += 1

        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.node_map:
            self.node_map[key].val = value
            self.get(key)
            return

        if len(self.node_map) == self.capacity:
            node = self.list_frequencies[self.lfu_count].popLeft()

            del self.node_map[node.key]
            del self.key_uses[node.key]

        node = ListNode(key, value)

        self.node_map[key] = node
        self.key_uses[key] = 1
        self.list_frequencies[1].insert(node)

        self.lfu_count = 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)