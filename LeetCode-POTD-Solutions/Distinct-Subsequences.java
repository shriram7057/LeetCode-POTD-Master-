1class Solution {
2    public int numDistinct(String s, String t) {
3        int m = s.length();
4        int n = t.length();
5
6        int[][] dp = new int[m + 1][n + 1];
7
8        // Base case: empty t can be formed in 1 way
9        for (int i = 0; i <= m; i++) {
10            dp[i][0] = 1;
11        }
12
13        // Fill DP table
14        for (int i = 1; i <= m; i++) {
15            for (int j = 1; j <= n; j++) {
16                if (s.charAt(i - 1) == t.charAt(j - 1)) {
17                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
18                } else {
19                    dp[i][j] = dp[i - 1][j];
20                }
21            }
22        }
23
24        return dp[m][n];
25    }
26}
27