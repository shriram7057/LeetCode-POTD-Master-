class Solution(object):
    def flatten(self, root):
        if not root:
            return
        self.prev = None
        def dfs(node):
            if not node:
                return
            dfs(node.right)
            dfs(node.left)
            node.right = self.prev
            node.left = None
            self.prev = node
        dfs(root)
