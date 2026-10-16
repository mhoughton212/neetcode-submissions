# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = before = curr = ListNode(0, head)

        for _ in range(left - 1):
            curr = curr.next
        
        to_reverse = curr.next
        tail = to_reverse
        prev = None

        for _ in range(right - left + 1):
            temp = to_reverse.next
            to_reverse.next = prev
            prev = to_reverse
            to_reverse = temp
        
        curr.next = prev
        tail.next = to_reverse

        return dummy.next
        