# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = res = ListNode()
        curr1, curr2 = l1, l2
        carry = 0
        while curr1 and curr2:
            res_val = carry + curr1.val + curr2.val
            carry = 1 if res_val > 9 else 0

            res.next = ListNode(res_val % 10)
            res = res.next
            curr1 = curr1.next
            curr2 = curr2.next
        
        while curr1:
            res_val = carry + curr1.val
            carry = 1 if res_val > 9 else 0

            res.next = ListNode(res_val % 10)
            res = res.next
            curr1 = curr1.next
        
        while curr2:
            res_val = carry + curr2.val
            carry = 1 if res_val > 9 else 0

            res.next = ListNode(res_val % 10)
            res = res.next
            curr2 = curr2.next
        
        if carry:
            res.next = ListNode(1)

        return dummy.next
        