class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, max_so_far):
            if not node:
                return 0

            good = 1 if node.val >= max_so_far else 0
            max_so_far = max(max_so_far, node.val)

            return good + dfs(node.left, max_so_far) + dfs(node.right, max_so_far)

        return dfs(root, root.val)
