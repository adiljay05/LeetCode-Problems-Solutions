# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode(-1)
        prev.next = head
        tmp = head
        while tmp:
            if prev.val == tmp.val:
                prev.next = tmp.next
            else:
                prev = tmp
            tmp = tmp.next
        return head
        