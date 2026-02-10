class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        cur = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        
        cur.next = list1 if list1 else list2
        return dummy.next
