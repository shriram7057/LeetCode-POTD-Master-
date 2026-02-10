1class Solution:
2    def minPathSum(self, grid):
3        m, n = len(grid), len(grid[0])
4        dp = [0] * n
5
6        dp[0] = grid[0][0]
7
8        # First row
9        for j in range(1, n):
10            dp[j] = dp[j - 1] + grid[0][j]
11
12        # Remaining rows
13        for i in range(1, m):
14            dp[0] += grid[i][0]
15            for j in range(1, n):
16                dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
17
18        return dp[-1]
19