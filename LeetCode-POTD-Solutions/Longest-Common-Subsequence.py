1class Solution(object):
2    def longestCommonSubsequence(self, text1, text2):
3        m, n = len(text1), len(text2)
4
5        # DP table of size (m+1) × (n+1)
6        dp = [[0] * (n + 1) for _ in range(m + 1)]
7
8        for i in range(1, m + 1):
9            for j in range(1, n + 1):
10                if text1[i - 1] == text2[j - 1]:
11                    dp[i][j] = dp[i - 1][j - 1] + 1
12                else:
13                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
14
15        return dp[m][n]
16