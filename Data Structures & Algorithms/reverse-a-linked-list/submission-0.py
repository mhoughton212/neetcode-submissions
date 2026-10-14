# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr: #None <- 1 <- 2  3 -> 4
            temp = curr.next #2
            curr.next = prev #None
            prev = curr #1
            curr = temp #2
        
        return prev