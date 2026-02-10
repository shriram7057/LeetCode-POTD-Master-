class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []
        res, q = [], [root]
        while q:
            size = len(q)
            for i in range(size):
                node = q.pop(0)
                if i == size - 1:
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res
