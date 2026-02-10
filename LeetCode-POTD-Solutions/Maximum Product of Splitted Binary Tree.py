# Maximum Product of Splitted Binary Tree
class Solution(object):
    def maxProduct(self, root):
        MOD = 10**9 + 7

        def sumTree(node):
            if not node:
                return 0
            return node.val + sumTree(node.left) + sumTree(node.right)

        total = sumTree(root)
        best = [0]

        def dfs(node):
            if not node:
                return 0
            s = node.val + dfs(node.left) + dfs(node.right)
            best[0] = max(best[0], s * (total - s))
            return s

        dfs(root)
        return best[0] % MOD
