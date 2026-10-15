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
        
        curr = head
        # [1,null] -> 
        # D -> 1 -> 2
        while curr:
            copy_curr = copy_map[curr]
            copy_curr.random = copy_map.get(curr.random)
            copy_curr.next = copy_map.get(curr.next)
            curr = curr.next

        return copy_map.get(head)
