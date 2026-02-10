class Solution(object):
    def reverseKGroup(self, head, k):
        dummy = ListNode(0, head)
        groupPrev = dummy

        def getKth(node, k):
            while node and k > 0:
                node = node.next
                k -= 1
            return node

        while True:
            kth = getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            prev, cur = kth.next, groupPrev.next
            while cur != groupNext:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp

        return dummy.next
