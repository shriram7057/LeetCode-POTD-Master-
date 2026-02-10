class Solution(object):
    def combine(self, n, k):
        res = []
        curr = []

        def backtrack(start):
            if len(curr) == k:
                res.append(list(curr))
                return

            for i in range(start, n + 1):
                curr.append(i)
                backtrack(i + 1)
                curr.pop()

        backtrack(1)
        return res
