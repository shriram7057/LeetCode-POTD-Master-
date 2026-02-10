1class Solution:
2    def minFallingPathSum(self, matrix):
3        n = len(matrix)
4        dp = matrix[0][:]  # copy first row
5
6        for i in range(1, n):
7            new_dp = [0] * n
8            for j in range(n):
9                best = dp[j]
10                if j > 0:
11                    best = min(best, dp[j - 1])
12                if j < n - 1:
13                    best = min(best, dp[j + 1])
14                new_dp[j] = matrix[i][j] + best
15            dp = new_dp
16
17        return min(dp)
18