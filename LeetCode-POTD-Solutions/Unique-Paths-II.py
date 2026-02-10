1class Solution:
2    def uniquePathsWithObstacles(self, obstacleGrid):
3        m, n = len(obstacleGrid), len(obstacleGrid[0])
4        dp = [0] * n
5
6        # Start position
7        dp[0] = 0 if obstacleGrid[0][0] == 1 else 1
8
9        for i in range(m):
10            for j in range(n):
11                if obstacleGrid[i][j] == 1:
12                    dp[j] = 0
13                else:
14                    if j > 0:
15                        dp[j] += dp[j - 1]
16
17        return dp[-1]
18