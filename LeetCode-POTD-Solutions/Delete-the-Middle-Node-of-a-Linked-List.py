# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteMiddle(self, head):
        if not head or not head.next:
            return None  # list becomes empty

        slow = head
        fast = head
        prev = None

        # Move fast by 2, slow by 1 → slow stops at middle
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Delete middle
        prev.next = slow.next

        return head
