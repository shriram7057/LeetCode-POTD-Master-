1class Solution:
2    def uniquePaths(self, m: int, n: int) -> int:
3        dp = [1] * n
4
5        for _ in range(1, m):
6            for j in range(1, n):
7                dp[j] += dp[j - 1]
8
9        return dp[-1]
10