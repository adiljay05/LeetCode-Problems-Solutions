/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeElements(ListNode head, int val) {
        if(head == null) return null;
        while(head!=null){
            if(head.val == val){
                head = head.next;
            }else{
                break;
            }
        }
        ListNode prev = head;
        if (prev == null)return null;
        while(prev.next!=null){
            if(prev.next.val==val){
                prev.next = prev.next.next;
            }else{
                prev=prev.next;
            }
        }
        return head;
    }
}