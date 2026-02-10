1class Solution:
2    def maxPathSum(self, root):
3        self.ans = float('-inf')
4
5        def dfs(node):
6            if not node:
7                return 0
8
9            # Max path sum from left/right child (ignore negative paths)
10            left = max(dfs(node.left), 0)
11            right = max(dfs(node.right), 0)
12
13            # Path passing through current node
14            self.ans = max(self.ans, node.val + left + right)
15
16            # Return max path going down
17            return node.val + max(left, right)
18
19        dfs(root)
20        return self.ans
21