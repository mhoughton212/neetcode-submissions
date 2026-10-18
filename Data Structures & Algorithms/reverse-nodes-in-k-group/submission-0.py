# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = before = ListNode(0, head)

        while True:
            check = before
            for _ in range(k):
                check = check.next
                if not check:
                    return dummy.next

            prev = None
            curr = before.next
            tail = curr

            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            before.next = prev
            tail.next = curr
            before = tail

    
