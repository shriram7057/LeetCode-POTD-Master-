1class Solution(object):
2    def rob(self, nums):
3        a = 0  # dp[i-2]
4        b = 0  # dp[i-1]
5
6        for money in nums:
7            c = max(b, a + money)
8            a, b = b, c
9
10        return b
11