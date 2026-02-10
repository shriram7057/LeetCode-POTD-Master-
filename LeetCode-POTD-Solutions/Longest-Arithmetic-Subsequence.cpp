1class Solution {
2public:
3    int longestArithSeqLength(vector<int>& nums) {
4        int n = nums.size();
5        if (n <= 2) return n;
6
7        vector<unordered_map<int, int>> dp(n);
8        int ans = 2;
9
10        for (int i = 0; i < n; i++) {
11            for (int j = 0; j < i; j++) {
12                int d = nums[i] - nums[j];
13                int len = 2;
14
15                if (dp[j].count(d)) {
16                    len = dp[j][d] + 1;
17                }
18
19                dp[i][d] = max(dp[i][d], len);
20                ans = max(ans, dp[i][d]);
21            }
22        }
23
24        return ans;
25    }
26};
27