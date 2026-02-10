class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        res = []

        for start, end in intervals:
            if not res or start > res[-1][1]:
                res.append([start, end])   # no overlap
            else:
                res[-1][1] = max(res[-1][1], end)   # merge overlap

        return res
