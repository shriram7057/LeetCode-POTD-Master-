class Solution(object):
    def createBinaryTree(self, descriptions):
        from collections import defaultdict

        nodes = {}
        child_set = set()

        for p, c, isLeft in descriptions:
            if p not in nodes:
                nodes[p] = TreeNode(p)
            if c not in nodes:
                nodes[c] = TreeNode(c)

            if isLeft == 1:
                nodes[p].left = nodes[c]
            else:
                nodes[p].right = nodes[c]

            child_set.add(c)

        for p, c, _ in descriptions:
            if p not in child_set:
                return nodes[p]
