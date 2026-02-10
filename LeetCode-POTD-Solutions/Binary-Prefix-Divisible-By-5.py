class Solution(object):
    def prefixesDivBy5(self, nums):
        res = []
        val = 0
        for b in nums:
            val = (val * 2 + b) % 5
            res.append(val == 0)
        return res
