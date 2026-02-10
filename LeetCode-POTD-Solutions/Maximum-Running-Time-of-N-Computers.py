1class Solution(object):
2    def maxRunTime(self, n, batteries):
3        batteries.sort()
4        left, right = 0, sum(batteries) // n
5
6        def can(t):
7            total = 0
8            for b in batteries:
9                total += min(b, t)
10            return total >= t * n
11
12        while left < right:
13            mid = (left + right + 1) // 2
14            if can(mid):
15                left = mid
16            else:
17                right = mid - 1
18
19        return left
20