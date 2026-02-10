class Solution(object):
    def numberOfPaths(self, grid, k):
        m, n = len(grid), len(grid[0])
        mod = 10**9 + 7
        dp = [[[0] * k for _ in range(n)] for _ in range(m)]
        dp[0][0][grid[0][0] % k] = 1
        for i in range(m):
            for j in range(n):
                for r in range(k):
                    if dp[i][j][r] == 0:
                        continue
                    nr = (r + grid[i][j]) % k
                if i > 0:
                    for r in range(k):
                        dp[i][j][(r + grid[i][j]) % k] = (dp[i][j][(r + grid[i][j]) % k] + dp[i-1][j][r]) % mod
                if j > 0:
                    for r in range(k):
                        dp[i][j][(r + grid[i][j]) % k] = (dp[i][j][(r + grid[i][j]) % k] + dp[i][j-1][r]) % mod
        return dp[m-1][n-1][0]
