class Solution:
    def combinationSum(self, candidates, target):
        res = []
        path = []

        def backtrack(start, total):
            if total == target:
                res.append(path[:])
                return
            if total > target:
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, total + candidates[i])
                path.pop()

        backtrack(0, 0)
        return res
