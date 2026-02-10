class Solution(object):
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)

        cur = root
        while True:
            if val < cur.val:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = TreeNode(val)
                    break
            else:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = TreeNode(val)
                    break

        return root
