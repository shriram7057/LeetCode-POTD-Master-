class Solution:
    def combine(self, n, k):
        res = []
        path = []

        def backtrack(start):
            if len(path) == k:
                res.append(path[:])
                return
            for num in range(start, n + 1):
                path.append(num)
                backtrack(num + 1)
                path.pop()

        backtrack(1)
        return res
