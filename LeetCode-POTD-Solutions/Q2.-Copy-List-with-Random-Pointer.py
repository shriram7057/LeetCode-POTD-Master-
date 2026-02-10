class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None

        # 1️⃣ Insert copied nodes after each original node
        curr = head
        while curr:
            newNode = Node(curr.val, curr.next)
            curr.next = newNode
            curr = newNode.next

        # 2️⃣ Assign random pointers for the copied nodes
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # 3️⃣ Separate the two lists
        curr = head
        newHead = head.next
        copy = newHead

        while curr:
            curr.next = curr.next.next
            if copy.next:
                copy.next = copy.next.next
            curr = curr.next
            copy = copy.next

        return newHead
