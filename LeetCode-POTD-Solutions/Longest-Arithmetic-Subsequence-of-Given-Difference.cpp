1class Solution {
2public:
3    int longestSubsequence(vector<int>& arr, int difference) {
4        unordered_map<int, int> dp;
5        int ans = 1;
6
7        for (int x : arr) {
8            dp[x] = dp[x - difference] + 1;
9            ans = max(ans, dp[x]);
10        }
11
12        return ans;
13    }
14};
15