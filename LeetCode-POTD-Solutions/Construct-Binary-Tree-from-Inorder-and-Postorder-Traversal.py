class Solution(object):
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None

        idx = {v: i for i, v in enumerate(inorder)}
        self.p = len(postorder) - 1

        def build(l, r):
            if l > r:
                return None
            val = postorder[self.p]
            self.p -= 1
            root = TreeNode(val)
            mid = idx[val]
            root.right = build(mid + 1, r)
            root.left = build(l, mid - 1)
            return root

        return build(0, len(inorder) - 1)
