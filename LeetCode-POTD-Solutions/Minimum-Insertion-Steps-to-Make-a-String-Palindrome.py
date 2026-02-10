1class Solution(object):
2    def minInsertions(self, s):
3        t = s[::-1]
4        n = len(s)
5
6        # DP for LCS(s, reverse(s))
7        dp = [[0] * (n + 1) for _ in range(n + 1)]
8
9        for i in range(1, n + 1):
10            for j in range(1, n + 1):
11                if s[i - 1] == t[j - 1]:
12                    dp[i][j] = dp[i - 1][j - 1] + 1
13                else:
14                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
15
16        lps = dp[n][n]
17        return n - lps
18