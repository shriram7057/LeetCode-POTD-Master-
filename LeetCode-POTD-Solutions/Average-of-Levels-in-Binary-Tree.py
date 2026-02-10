class Solution(object):
    def averageOfLevels(self, root):
        res = []
        q = [root]
        while q:
            level_sum = 0
            size = len(q)
            for _ in range(size):
                node = q.pop(0)
                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level_sum / float(size))
        return res
