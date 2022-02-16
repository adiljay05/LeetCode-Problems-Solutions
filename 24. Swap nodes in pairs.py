# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: # if there is no or single element in the list
            return head
        """
        Cur is pointing 0th index
        cur_next pointing 1st index
        
        swap values and set cur to 2nd index
        if second index has values set cur_next to 3rd index
        
        keep swapping until one of the node give None value
        """
        cur = head # current node
        cur_next = cur.next # next to current node (considering pair of current and next node)
        while cur and cur_next: #keep swapping until current and next node has values
            """Swap the value of current node with next node"""
            tmp = cur.val
            cur.val = cur_next.val
            cur_next.val=tmp
            """Move current node ptr to next of next node -> cur=cur.next.next"""
            cur=cur_next.next
            """If current node has value, set -> cur.next = cur.next.next.next"""
            if cur:
                cur_next = cur.next
        return head
