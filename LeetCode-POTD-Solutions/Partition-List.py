class Solution(object):
    def partition(self, head, x):
        small = ListNode(0)
        big = ListNode(0)
        s = small
        b = big

        while head:
            if head.val < x:
                s.next = head
                s = s.next
            else:
                b.next = head
                b = b.next
            head = head.next

        b.next = None
        s.next = big.next
        return small.next
