class Solution(object):
    def subsets(self, nums):
        res = []

        def backtrack(i, path):
            if i == len(nums):
                res.append(list(path))
                return
            backtrack(i + 1, path)
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

        backtrack(0, [])
        return res
