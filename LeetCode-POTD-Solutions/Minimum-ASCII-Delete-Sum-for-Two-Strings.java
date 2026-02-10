1class Solution {
2    public int minimumDeleteSum(String s1, String s2) {
3        int m = s1.length();
4        int n = s2.length();
5
6        int[][] dp = new int[m + 1][n + 1];
7
8        // Base cases: delete all characters
9        for (int i = 1; i <= m; i++) {
10            dp[i][0] = dp[i - 1][0] + s1.charAt(i - 1);
11        }
12        for (int j = 1; j <= n; j++) {
13            dp[0][j] = dp[0][j - 1] + s2.charAt(j - 1);
14        }
15
16        // Fill DP table
17        for (int i = 1; i <= m; i++) {
18            for (int j = 1; j <= n; j++) {
19                if (s1.charAt(i - 1) == s2.charAt(j - 1)) {
20                    dp[i][j] = dp[i - 1][j - 1];
21                } else {
22                    dp[i][j] = Math.min(
23                        dp[i - 1][j] + s1.charAt(i - 1),
24                        dp[i][j - 1] + s2.charAt(j - 1)
25                    );
26                }
27            }
28        }
29
30        return dp[m][n];
31    }
32}
33