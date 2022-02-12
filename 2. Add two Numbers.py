# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        mm = ListNode()
        m = mm
        carry = 0
        while l1 or l2 or carry: # iterate until elements in one of the list or carry has value
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            
            sum_ = v1+v2+carry
            carry = int(sum_/10)
            m.next = ListNode(sum_%10)
            
            m = m.next                
            
        return mm.next
            
        