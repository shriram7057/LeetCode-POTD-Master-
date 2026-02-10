1class Solution(object):
2    def maxUncrossedLines(self, nums1, nums2):
3        m, n = len(nums1), len(nums2)
4
5        dp = [[0] * (n + 1) for _ in range(m + 1)]
6
7        for i in range(1, m + 1):
8            for j in range(1, n + 1):
9                if nums1[i - 1] == nums2[j - 1]:
10                    dp[i][j] = dp[i - 1][j - 1] + 1
11                else:
12                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
13
14        return dp[m][n]
15