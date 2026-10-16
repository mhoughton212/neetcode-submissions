class MyCircularQueue:
    class Node:
        def __init__(self, x: int = 0, next: 'Node' = None):
            self.val = x
            self.next = next

    def __init__(self, k: int):
        self.size = 0
        self.capacity = k
        self.head = self.tail = self.Node()

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        node = self.Node(value) 
        if self.isEmpty():
            self.head.next = node
            self.head = self.head.next 
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = self.tail.next

        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.size -= 1
        if self.isEmpty():
            self.head = self.tail = self.Node()
        else:
            self.head = self.head.next
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.val
        
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()