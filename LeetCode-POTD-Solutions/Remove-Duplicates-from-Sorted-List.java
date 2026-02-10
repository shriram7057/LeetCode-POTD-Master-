class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode current = head;
        
        while (current != null && current.next != null) {
            if (current.val == current.next.val) {
                current.next = current.next.next;  // skip duplicate
            } else {
                current = current.next;            // move ahead
            }
        }
        
        return head;
    }
}
