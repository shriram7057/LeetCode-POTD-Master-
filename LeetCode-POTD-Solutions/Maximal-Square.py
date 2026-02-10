1class Solution:
2    def maximalSquare(self, matrix):
3        if not matrix:
4            return 0
5
6        m, n = len(matrix), len(matrix[0])
7        dp = [0] * (n + 1)
8        max_side = 0
9        prev = 0  # dp[i-1][j-1]
10
11        for i in range(1, m + 1):
12            for j in range(1, n + 1):
13                temp = dp[j]
14                if matrix[i - 1][j - 1] == '1':
15                    dp[j] = min(dp[j], dp[j - 1], prev) + 1
16                    max_side = max(max_side, dp[j])
17                else:
18                    dp[j] = 0
19                prev = temp
20
21        return max_side * max_side
22