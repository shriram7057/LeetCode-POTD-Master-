class Solution(object):
    def deleteNode(self, root, key):

        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            cur = root.right
            while cur.left:
                cur = cur.left

            root.val = cur.val
            root.right = self.deleteNode(root.right, cur.val)

        return root
