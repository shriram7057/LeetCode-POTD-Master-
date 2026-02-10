class Solution(object):
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        idx = {v: i for i, v in enumerate(inorder)}
        self.p = 0

        def build(l, r):
            if l > r:
                return None
            val = preorder[self.p]
            self.p += 1
            root = TreeNode(val)
            mid = idx[val]
            root.left = build(l, mid - 1)
            root.right = build(mid + 1, r)
            return root

        return build(0, len(inorder) - 1)
