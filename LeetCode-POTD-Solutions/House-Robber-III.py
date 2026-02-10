1class Solution:
2    def rob(self, root):
3        def dfs(node):
4            if not node:
5                return (0, 0)
6
7            left_rob, left_not = dfs(node.left)
8            right_rob, right_not = dfs(node.right)
9
10            # If we rob this node, we cannot rob children
11            rob = node.val + left_not + right_not
12
13            # If we don't rob this node, we can choose best of children
14            not_rob = max(left_rob, left_not) + max(right_rob, right_not)
15
16            return (rob, not_rob)
17
18        return max(dfs(root))
19