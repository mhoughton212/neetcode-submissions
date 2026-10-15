# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left_lol: int, right_lol: int) -> Optional[ListNode]:
        dummy = prev = curr = ListNode(0, head)

        for _ in range(left_lol):
            curr = curr.next
        
        left = curr

        for _ in range(right_lol - left_lol):
            curr = curr.next
        right = curr

        curr = head
        while curr != left:
            prev = curr
            curr = curr.next

        stable_prev = prev
        stable_curr = curr
        after = right.next
        while curr != after:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        stable_prev.next = prev
        stable_curr.next = curr

        return dummy.next
        