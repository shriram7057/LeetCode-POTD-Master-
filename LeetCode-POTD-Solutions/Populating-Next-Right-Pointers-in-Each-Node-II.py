class Solution(object):
    def connect(self, root):
        if not root:
            return root

        cur = root
        while cur:
            dummy = Node(0)
            tail = dummy
            while cur:
                if cur.left:
                    tail.next = cur.left
                    tail = tail.next
                if cur.right:
                    tail.next = cur.right
                    tail = tail.next
                cur = cur.next
            cur = dummy.next

        return root
