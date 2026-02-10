1class Solution:
2    def numSquares(self, n: int) -> int:
3        dp = [float('inf')] * (n + 1)
4        dp[0] = 0
5
6        for i in range(1, n + 1):
7            j = 1
8            while j * j <= i:
9                dp[i] = min(dp[i], dp[i - j * j] + 1)
10                j += 1
11
12        return dp[n]
13