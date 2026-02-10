1class Solution:
2    def longestPalindromeSubseq(self, s: str) -> int:
3        n = len(s)
4        dp = [[0] * n for _ in range(n)]
5
6        # Single characters are palindromes of length 1
7        for i in range(n):
8            dp[i][i] = 1
9
10        # Build DP for substrings of increasing length
11        for length in range(2, n + 1):
12            for i in range(n - length + 1):
13                j = i + length - 1
14                if s[i] == s[j]:
15                    dp[i][j] = 2 + (dp[i + 1][j - 1] if i + 1 <= j - 1 else 0)
16                else:
17                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
18
19        return dp[0][n - 1]
20