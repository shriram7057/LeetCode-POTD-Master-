1class Solution {
2    public int minDistance(String word1, String word2) {
3        int m = word1.length();
4        int n = word2.length();
5
6        int[][] dp = new int[m + 1][n + 1];
7
8        // Base cases
9        for (int i = 0; i <= m; i++) {
10            dp[i][0] = i; // delete all characters
11        }
12        for (int j = 0; j <= n; j++) {
13            dp[0][j] = j; // insert all characters
14        }
15
16        // Fill DP table
17        for (int i = 1; i <= m; i++) {
18            for (int j = 1; j <= n; j++) {
19                if (word1.charAt(i - 1) == word2.charAt(j - 1)) {
20                    dp[i][j] = dp[i - 1][j - 1];
21                } else {
22                    dp[i][j] = 1 + Math.min(
23                        dp[i - 1][j - 1], // replace
24                        Math.min(
25                            dp[i - 1][j],   // delete
26                            dp[i][j - 1]    // insert
27                        )
28                    );
29                }
30            }
31        }
32
33        return dp[m][n];
34    }
35}
36