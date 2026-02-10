1class Solution:
2    def firstBadVersion(self, n: int) -> int:
3        left, right = 1, n
4
5        while left < right:
6            mid = left + (right - left) // 2
7            if isBadVersion(mid):
8                right = mid
9            else:
10                left = mid + 1
11
12        return left
13