class Solution(object):
    def deleteDuplicates(self, head):
        dummy = ListNode(0, head)
        cur = dummy

        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                val = cur.next.val
                while cur.next and cur.next.val == val:
                    cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next
