"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        copy_map = {}

        while curr:
            copy_map[curr] = Node(curr.val)
            curr = curr.next
        
        dummy = copy_curr = Node(0)
        curr = head
        # [1,null] -> 
        # D -> 1 -> 2
        while curr:
            copy_curr.next = copy_map[curr]
            copy_curr.next.random = copy_map.get(curr.random)
            curr = curr.next
            copy_curr = copy_curr.next

        return dummy.next
