class Solution(object):
    def insertionSortList(self, head):
        if not head:
            return head

        dummy = ListNode(0)
        curr = head

        while curr:
            prev = dummy

            # find position to insert curr
            while prev.next and prev.next.val < curr.val:
                prev = prev.next

            nextNode = curr.next
            curr.next = prev.next
            prev.next = curr
            curr = nextNode

        return dummy.next
