# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        slow.next = None
        
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        # 2 -> 8 -> 4 ->6 -> None
        # 2 4*
        # 6* 8
        front, back = head, prev
        while front and back:
            temp = front.next #None
            front.next = back 
            temp_back = back.next #None
            back.next = temp
            front = temp
            back = temp_back
    