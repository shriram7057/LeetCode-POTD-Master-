class Solution(object):
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        res = []
        for s, e in intervals:
            if not res or s > res[-1][1]:
                res.append([s, e])
            else:
                res[-1][1] = max(res[-1][1], e)
        return res
