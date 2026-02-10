class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.ans = 0

        def dfs(node, go_left, length):
            if not node:
                return

            self.ans = max(self.ans, length)

            if go_left:
                # go left next → zigzag continues
                dfs(node.left, False, length + 1)
                # restart zigzag on right
                dfs(node.right, True, 1)
            else:
                # go right next → zigzag continues
                dfs(node.right, True, length + 1)
                # restart zigzag on left
                dfs(node.left, False, 1)

        # Start DFS: one assuming first move is left, one right
        dfs(root, True, 0)
        dfs(root, False, 0)

        return self.ans
