1class Solution {
2    public int minOperations(int[] nums, int k) {
3        long sum = 0;
4        for (int x : nums) sum += x;
5
6        int r = (int)(sum % k);
7        if (r == 0) return 0;
8
9        // dp[d] = minimum cost to reduce total by d
10        int[] dp = new int[r + 1];
11        final int INF = (int)1e9;
12        for (int i = 1; i <= r; i++) dp[i] = INF;
13        dp[0] = 0;
14
15        for (int x : nums) {
16            // We can reduce x by 1..x but only care up to r
17            for (int d = r; d >= 0; d--) {
18                if (dp[d] == INF) continue;
19                int limit = Math.min(x, r - d);
20                if (limit > 0) {
21                    int nd = d + limit;
22                    dp[nd] = Math.min(dp[nd], dp[d] + limit);
23                }
24            }
25        }
26
27        return dp[r];
28    }
29}
30